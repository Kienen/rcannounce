from django.shortcuts import render
from participant.forms import *
import account.views

# Create your views here.
class SignupView(account.views.SignupView):

    form_class = SignupForm

    def generate_username(self, form):
        username = form.fields['email']
        return username


def home_page(request):
    return render(request, 'home.html')

