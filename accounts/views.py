from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView as BaseLoginView


from accounts.forms import SignupForm

class LoginView(BaseLoginView):
    template_name = 'login.html'

# Create your views here.
class SignupView(FormView):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form':form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

        return render(request, 'signup.html', {'form':form})
