from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from . import models
# Create your views here.
def method1 (request):
    return render(request,'index.html',{})
def home(request):
    return render(request,'index.html',{})
def login(request):
    return render(request,'login.html',{})
def forhospital(request):
    return render(request,'forhospital.html',{})
def Services(request):
    return render(request,'Services.html',{})
def about(request):
    return render(request,'about.html',{})
def contact(request):
    return render(request,'contact.html',{})
def signup(request):
    return render(request,'signup.html',{})
def signup2(request):
    return render(request,'signup2.html',{})
def userlogin(request):
    v1 = request.POST['email']
    v2 = request.POST['pass']
    obj = models.userdata.objects.all()
    for data in obj:
        v3 = data.useremail
        v4 = data.userpassword
        if v1 == v3 and v2 == v4:
            return render(request, 'filter.html', {})
    else:
        return render(request, 'login.html', {'massage':'''The username and password you entered did not match our records. Please double-check 
                            and try again'''})

def hospitallogin(request):
    v1 = request.POST['email']
    v2 = request.POST['pass']
    obj = models.hospitaldata.objects.all()
    for d in obj:
        v3 = d.hospitalemail
        v4 = d.hospitalpassword
        if v3 == v1 and v4 == v2:
            return render(request, 'hospitaldata.html', {})
    else:
        return render(request, 'login.html', {'massage': '''! The username and password you entered did not match our records. Please double-check 
                                    and try again'''})


def userdata(request):
    v1 = request.POST['name']
    v2 = request.POST['number']
    v3 = request.POST['email']
    v4 = request.POST['Gender']
    v5 = request.POST['date']
    v6 = request.POST['pass']
    v7 = request.POST['repass']
    if v6 == v7 :
        userdata = models.userdata(username=v1, usernumber=v2, useremail=v3, gender=v4, userdate=v5, userpassword=v6)
        userdata.save()
        return render(request, 'filter.html', {})
    else:
        return HttpResponse('The password does not match')
def hospitaldata(request):
    v1 = request.POST['name']
    v2 = request.POST['email']
    v3 = request.POST['enumber']
    v4 = request.POST['count']
    v5 = request.POST['location']
    v6 = request.POST['image']
    v7 = request.POST['pass']
    v8 = request.POST['repass']
    if v7 == v8 :
        hospitaldata = models.hospitaldata(hospitalname=v1, hospitalemail=v2, EmergencyNumber=v3, Emergencycount= v4,
                                           location=v5, image=v6, hospitalpassword=v7)
        hospitaldata.save()
        return render(request, 'hospitaldata.html', {'massage':v1})
    else:
        return HttpResponse('The password does not match')

def contactdata(request):
    v1 = request.POST['name']
    v2 = request.POST['email']
    try:
        v3 = request.POST['subject']
    except:
        v3 ='null'
    v4 = request.POST['massage']
    contactdata = models.contactldata(contactalname=v1, contactemail=v2, contactsubject=v3, contactmassage=v4)
    contactdata.save()
    #return render(request, 'contact.html', {})
    return HttpResponseRedirect('/')
def hospitaldata2(request):
    # v0 = request.POST['email']
    v1 = request.POST['name']
    v2 = request.POST['description']
    # v3 = request.POST['email']
    hospitaldata = models.hospitaldata2(deptname=v1, deptdescription=v2)
    hospitaldata.save()
    data = models.hospitaldata2.objects.all()
    return render(request, 'hospitaldata.html', {'data':data})
def filter (request ):
    v1 = request.POST['dept']
    v2 = request.POST['info_form_doc']
    obj = models.hospitaldata2.objects.all()
    for data in obj:
        v3 = data.deptname
    if v1 == v3 :
        return render(request, 'Filter.html', {'massage': data.deptname})
