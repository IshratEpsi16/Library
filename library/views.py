from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import admin_info,student_signup,admin_student_connect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . import forms
# Create your views here.
def home(request):
    context={}
    return render(request,'library/home.html',context)
def admin_all_info(request):
    info_show = admin_info.objects.all()
    obj1 = forms.admin_form()
    if request.method == "POST":
        obj1 = forms.admin_form(request.POST)
        if obj1.is_valid():
            obj1.save(commit=True)
            return HttpResponseRedirect(reverse('library:admin_info'))
    context = {'key':obj1,'info_show':info_show}
    return render(request,'library/admin_info.html',context)
def student_signup_form(request):
    registerd = False
    
    if request.method == "POST":
        student_form_obj = forms.student_form(data = request.POST)
        user_obj = forms.user_built_in(data = request.POST)
        if user_obj.is_valid() and student_form_obj.is_valid():
            #built in User class
            user = user_obj.save()
            user.set_password(user.password)
            user.save()
            #my created class
            student_form_obj_2 = student_form_obj.save(commit=False)
            student_form_obj_2.user = user
            if 'pic' in request.FILES:
                student_form_obj_2.pic = request.FILES['pic']

            student_form_obj_2.save()
            registerd = True
    else:
        student_form_obj = forms.student_form()
        user_obj = forms.user_built_in()

    context = {'student_form_obj' : student_form_obj,'user_obj':user_obj,'registerd':registerd}
    return render(request,'library/student_signup.html',context)
def admin_dashboard(request):
   
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        #user_more_info = student_signup.objects.get(user__pk=user_id)

    context = {}
    return render(request,'library/admin_dashboard.html',context)
def student_info(request):
    info_show = student_signup.objects.all()
    context = {'info_show':info_show}
    return render(request,'library/student_info.html',context)
def issue_book(request):
    issue_obj = admin_student_connect.objects.all()
    issue_obj2 = forms.admin_student_connect()
    issue_obj3 = student_signup.objects.all()
    if request.method == "POST":
        issue_obj2 = forms.admin_student_connect(request.POST)
        if issue_obj2.is_valid():
            issue_obj2.save(commit=True)
            return HttpResponseRedirect(reverse('library:issue_book'))
    context = {'issue_obj':issue_obj,'issue_obj2':issue_obj2,'issue_obj3':issue_obj3}
    return render(request,'library/issue_book.html',context)
def student_dashboard(request):
    
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = student_signup.objects.get(user__pk=user_id)
        
        
    
        
        
    context = {'user_basic_info':user_basic_info,'user_more_info':user_more_info}
    return render(request,'library/student_dashboard.html',context)
def my_profile(request):
    
    context = {}
    return render(request,'library/my_profile.html',context)
#update/edit
def edit(request,id):
    edit_obj = admin_student_connect.objects.get(pk=id)
    new_obj = forms.admin_student_connect(instance=edit_obj)
    if request.method == "POST":
        new_obj = forms.admin_student_connect(request.POST, instance=edit_obj)
        if new_obj.is_valid():
            new_obj.save(commit=True)
            return HttpResponseRedirect(reverse('library:issue_book'))
    context = {'edit_obj' : edit_obj, 'new_obj' : new_obj}
    return render(request,'library/edit.html',context)
#delete
def delete_fun(request,id):
    del_obj = admin_student_connect.objects.get(pk=id).delete()
    context = {'del_obj':del_obj}
    return render(request,'library/delete.html',context)
def admin_login(request):
    return render(request,'library/admin_login.html',context={})

def admin_login_fun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('library:admin_dashboard'))
            else:
                return HttpResponse('Not Authenticated')
        else:
            return HttpResponse('Wrong Information!!')
    else:
        

        context = {}
        return HttpResponseRedirect(reverse('library:admin_login'))
@login_required()
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('library:home'))
def student_login(request):
    return render(request,'library/student_login.html',context = {})
def student_login_fun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('library:student_dashboard'))
            else:
                return HttpResponse('Your account is not active')
        else:
            return HttpResponse('Wrong information!!')
    else:
        context = {}
        return render(request,'library/student_login.html',context)
@login_required
def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('library:home'))