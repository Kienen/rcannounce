from django.shortcuts import render
from django.contrib.auth.models import User
from participant.forms import *
import account.views

# Create your views here.
class SignupView(account.views.SignupView):

    form_class = SignupForm

    def generate_username(self, form):
        username = form['email'].value()[0:29].lower()
        username = ''.join([x for x in username if x not in "!#$%&'*+-/=?^_`{|}~}"])
        i=0
        while User.objects.filter(username=username):
            if i < 10:
                username=str(i) + username[1:]
            else:
                username=str(i) + username[2:]
            i+=1
        return username


def home_page(request):
    return render(request, 'home.html')

