from django.shortcuts import render
from user.models import UserRegistrationModel
from django.contrib import messages
from user.forms import UserRegistrationForm

def index(request):
    return render(request,"index.html")
def adminlogin(request):
    return render(request,"adminlogin.html")


def UserLogin(request):
    return render(request, 'userlogin.html', {})

def UserRegister(request):
    form = UserRegistrationForm()
    return render(request, 'Register.html', {'form': form})



def UserRegisterAction(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            # return HttpResponseRedirect('./CustLogin')
            form = UserRegistrationForm()
            return render(request, 'Register.html', {'form': form})
        else:
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'Register.html', {'form': form})


