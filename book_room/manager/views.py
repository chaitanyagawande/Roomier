from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import RoomForm, TimeSlotForm, TimeSlotUpdateForm
from .models import Room, TimeSlot, AdvanceBooking
from accounts.decorators import manager_required
from customer.models import TimeSlotBook, TimeSlotCancel

from accounts.decorators import customer_required

decorators = [manager_required, login_required]


@method_decorator(decorators, name="dispatch")
class RoomCreateView(CreateView):
    model = Room
    template_name = "manager/add_room.html"
    form_class = RoomForm

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        try:
            form.save()
            return super(RoomCreateView, self).form_valid(form)
        except:
            messages.add_message(self.request, messages.WARNING, 'Room Already Exists.')
            return redirect("/manager/create_room/")

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Room Created Successfully.')
        success_url = '/manager/room/' + str(self.object.pk)
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.filter(room_owner=self.request.user)
        return context


decorators = [manager_required, login_required]


@method_decorator(decorators, name="dispatch")
class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy("manager:create_room")

    def get_object(self, *args, **kwargs):
        return Room.objects.get(id=self.kwargs["room_id"])

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Room Successfully Deleted.')
        success_url = '/manager/create_room/'
        return success_url


decorators = [manager_required, login_required]


@method_decorator(decorators, name="dispatch")
class TimeSlotView(CreateView):
    model = TimeSlot
    template_name = "manager/add_time_slot.html"
    form_class = TimeSlotForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.time_slot_owner = self.request.user
        form.instance.room_id = Room.objects.get(id=self.kwargs.get("room_id"))
        try:
            form.save()
            return super(TimeSlotView, self).form_valid(form)
        except:
            messages.add_message(self.request, messages.WARNING, 'Time Slot Already Exists.')
            return redirect("/manager/room/" + self.kwargs.get("room_id") + "/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_slot'] = TimeSlot.objects.filter(time_slot_owner=self.request.user,
                                                       room_id=Room.objects.get(id=self.kwargs.get("room_id")))
        return context

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Successfully Created Time Slot.')
        success_url = '/manager/room/' + str(self.kwargs.get("room_id"))
        return success_url


@login_required
@manager_required
def TimeSlotUpdateView(request, room_id, slot_id, *args, **kwargs):
    if request.method == 'POST':
        form = TimeSlotUpdateForm(data=request.POST, instance=get_object_or_404(TimeSlot, id=slot_id))
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.INFO, 'Time Slot Updated Successfully.')
                return redirect("/manager/room/" + str(room_id))
            except:
                messages.add_message(request, messages.ERROR, 'Time Slot Already Exists.')
                return redirect("/manager/room/" + str(room_id))


    else:
        form = TimeSlotUpdateForm(instance=request.user)
        ts = TimeSlot.objects.get(id=slot_id)
        return render(request, 'manager/edit_time_slot.html', {'form': form, "slot": ts})


decorators = [manager_required, login_required]


@method_decorator(decorators, name="dispatch")
class TimeSlotDeleteView(DeleteView):
    model = TimeSlot

    def get_object(self, *args, **kwargs):
        return TimeSlot.objects.get(id=self.kwargs["slot_id"])

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Successfully Deleted Time Slot.')
        success_url = '/manager/room/' + str(self.kwargs.get("room_id"))
        return success_url


decorators = [manager_required, login_required]


@method_decorator(decorators, name="dispatch")
class BookingHistory(DetailView):
    model = TimeSlotBook
    template_name = "manager/booking_history.html"

    def get(self, request):
        tsb1 = TimeSlotBook.objects.filter(manager_id=self.request.user)
        tsb2 = TimeSlotCancel.objects.filter(manager_id=self.request.user)
        return render(request, self.template_name, {"booked": tsb1, "cancelled": tsb2})


@login_required
@manager_required
def EditAdvanceDays(request):
    if request.method == 'POST':
        no_of_days = request.POST["book_days"]
        user = AdvanceBooking.objects.get(manager_id=request.user)
        user.no_of_days = no_of_days
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Updated Successfully.')
        return redirect("/accounts/profile/")
    else:
        messages.add_message(request, messages.ERROR, 'Login As Manager.')
        logout(request)
        return redirect("/accounts/login/")
