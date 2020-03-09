from datetime import datetime, date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from accounts.models import User
from manager.models import TimeSlot, Room
from customer.models import TimeSlotBook, TimeSlotCancel
from accounts.decorators import customer_required
from manager.models import AdvanceBooking


def IndexPageView(request):
    return render(request, "index.html")


def SearchTimeSlot(request):
    return render(request, 'customer/search_time_slot.html')


decorators = [customer_required, login_required]


@method_decorator(decorators, name="dispatch")
class SearchView(ListView):
    model = TimeSlot
    template_name = "customer/search_results.html"

    def get(self, request):
        start_time = self.request.GET["start_time"]
        end_time = self.request.GET["end_time"]
        date = self.request.GET["date"]
        time_slot = self.get_queryset().filter(start_time=start_time, end_time=end_time)
        return render(request, self.template_name, {'time_slot': time_slot, 'date': date})


decorators = [customer_required, login_required]


@method_decorator(decorators, name="dispatch")
class BookView(CreateView):
    model = TimeSlotBook
    template_name = "customer/slot_book.html"

    def post(self, request):
        owner_room = User.objects.get(id=self.request.POST["owner"])
        start_time = self.request.POST["start_time"]
        end_time = self.request.POST["end_time"]
        room_id = Room.objects.get(id=self.request.POST["room_id"])
        date1 = self.request.POST["date"]
        d = str(date1)
        d = d.replace("-", "")
        cus_date = datetime.strptime(d, "%Y%m%d").date()
        today = datetime.today().date()
        today = str(today)
        today = today.replace("-", "")
        today = datetime.strptime(today, "%Y%m%d").date()
        day = (cus_date - today).days
        adb = AdvanceBooking.objects.get(manager_id=owner_room)
        days = adb.no_of_days
        if days >= day >= 0:
            try:
                tsb = TimeSlotBook(manager_id=owner_room, customer_id=self.request.user, date=date1, room_id=room_id,
                                   start_time=start_time, end_time=end_time)
                tsb.save()
                messages.add_message(request, messages.SUCCESS, 'Time Slot Successfully Booked.')
                return redirect("/customer/book/")
            except:
                messages.add_message(request, messages.WARNING, 'Time Slot Already Booked.')
                return redirect("/customer/search/?date=" + str(date1) + "&start_time=" + start_time +
                                "&end_time=" + end_time)
        messages.add_message(request, messages.ERROR, 'Time Slot Can Booked Before ' + str(days) + 'days.')
        return redirect("/customer/search/?date=" + str(date1) + "&start_time=" + start_time +
                        "&end_time=" + end_time)


dispatcher = [login_required, customer_required]


@method_decorator(dispatcher, name="dispatch")
class BookDetailView(DetailView):
    model = TimeSlotBook
    template_name = "customer/time_slot_book.html"

    def get(self, request):
        tsb1 = TimeSlotBook.objects.filter(customer_id=self.request.user)
        tsb2 = TimeSlotCancel.objects.filter(customer_id=self.request.user)
        return render(request, self.template_name, {"booked": tsb1, "cancelled": tsb2})


decorators = [customer_required, login_required]


@method_decorator(decorators, name="dispatch")
class CancelView(UpdateView):
    model = TimeSlotBook
    template_name = "customer/time_slot_book.html"

    def post(self, request):
        slot_id = self.request.POST["slot_id"]
        tsb = TimeSlotBook.objects.get(id=slot_id)
        tsc = TimeSlotCancel(manager_id=tsb.manager_id, customer_id=tsb.customer_id, date=tsb.date, room_id=tsb.room_id,
                             start_time=tsb.start_time, end_time=tsb.end_time)
        tsc.save()
        TimeSlotBook.objects.get(id=slot_id).delete()
        messages.add_message(request, messages.SUCCESS, 'Time Slot Cancelled Successfully.')
        return redirect("/customer/book/")


@method_decorator(login_required, name="dispatch")
class ProfileView(DetailView):
    model = User
    template_name = 'manager/profile.html'

    def get_user_profile(self, username):
        return get_object_or_404(User, pk=username)
