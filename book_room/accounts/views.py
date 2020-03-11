from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView
from .forms import ManagerSignUpForm, CustomerSignUpForm, UpdateProfileForm
from .models import User
from django.contrib.auth.decorators import login_required
from manager.models import AdvanceBooking
from django.http import HttpResponseServerError, HttpResponse


class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'registration/manager_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        AdvanceBooking.objects.create(manager_id=User.objects.get(id=user.id))
        login(self.request, user)
        return redirect('accounts:profile')

    def form_invalid(self, form):
        pass


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:profile')


@login_required
def get_user_profile(request):
    user = User.objects.get(username=request.user.username)
    if user.is_manager:
        adb = AdvanceBooking.objects.get(manager_id=request.user)
        return render(request, 'profile.html', {"user": user, "no_of_days":adb})
    else:
        return render(request, 'profile.html', {"user": user})


@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        messages.add_message(request, messages.INFO, 'Your Profile has been successfully updated!.')
        return redirect("/accounts/profile/")
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)
            messages.add_message(request, messages.INFO, 'Your password was successfully updated!.')
            return redirect('/accounts/login/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })

