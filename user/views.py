from django.contrib import messages
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
from user.forms import UserRegistrationForm
from user.models import UserRegistrationModel, UserFirstImageModel, UserSecondImageModel


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'user/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'userlogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'userlogin.html', {})



def UserHome(request):
    return render(request,"user/UserHomePage.html",{})


def UserUploadImageForm(request):
    loginid = request.session['loginid']
    data = UserFirstImageModel.objects.filter(username= loginid)
    return render(request,"user/UploadImageform.html", {"data": data})


def UserImageProcessFirst(request):
    if request.method== 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        from .utility.ImageRecognition import Recognitions
        obj = Recognitions()
        resultDict = obj.start_process(filename)
        resultDict = str(resultDict)
        print('Result:', resultDict)
        loginid = request.session['loginid']
        email = request.session['email']
        UserFirstImageModel.objects.create(username=loginid, email=email, filename=filename, results=resultDict, file=uploaded_file_url)
        messages.success(request, 'Image Processed Success')
        print("File Image Name "+uploaded_file_url)
        data = UserFirstImageModel.objects.filter(username=loginid)
        return render(request, "user/UploadImageform.html", {"data": data})



def UserImageAIForm(request):
    loginid = request.session['loginid']
    data = UserSecondImageModel.objects.filter(username=loginid)
    return render(request, "user/UserImageAI.html", {"data": data})

def ProcessUserImageAI(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        from .utility.ImageAiPredict import run_inference
        resultDict = run_inference(filename)
        print('Result:', resultDict)
        loginid = request.session['loginid']
        email = request.session['email']
        UserSecondImageModel.objects.create(username=loginid, email=email, filename=filename, results=resultDict,
                                           file=uploaded_file_url)
        messages.success(request, 'Image Processed Success')
        print("File Image Name " + uploaded_file_url)
        data = UserSecondImageModel.objects.filter(username=loginid)
        return render(request, "user/UserImageAI.html", {"data": data})


def StartTraining(request):
    from .utility import ImageAiPredict
    ImageAiPredict.train_network()
    return render(request, "user/UserHomePage.html", {})
