from django.shortcuts import render,redirect,reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login,logout
from django.views.generic.edit import CreateView
from user.forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

class LoginView(LoginView):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_access = request.user.user_access
            if user_access == "superadmin":
                return redirect('vehicles:view1')
            elif user_access == "admin":
                return redirect('vehicles:view2')
            elif user_access == "user":
                return redirect('vehicles:view3')

        return super().get(request, *args, **kwargs)

class LogoutView(LogoutView):
    success_url = reverse_lazy('vehicles:home')

