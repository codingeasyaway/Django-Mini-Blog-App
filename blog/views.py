from django.contrib.auth import authenticate ,login,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group


# Create your views here.

# Home Page
def Index(request):
    title= 'Home - MiniBlog'
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts,'title':title})

# About Page
def About(request):
    title = 'About - MiniBlog'
    return render(request,'blog/about.html',{'title':title})

# Contact Page
def Contact(request):
    title = 'Contact - MiniBlog'
    return render(request,'blog/contactus.html', {'title': title})

# Dashboard Page
def Dashboard(request):
    title = 'My Profile'
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        grp = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':grp,'title':title})
    else:
        return HttpResponseRedirect('/User_Login/')

# Add Post Page
def AddPost(request):
    title = 'Add Post - MiniBlog'
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['Desc']
                pst = Post(title=title, Desc=desc)
                messages.success(request, "Add Post Successfully !! ")
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/User_Login/')

# Update Post Page
def UpdatePost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                messages.success(request,"Update Post Successfull !! ")
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/User_Login/')

# Delete Post
def DeletePost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/Dashboard/')
    else:
        return HttpResponseRedirect('/User_Login/')

# Signup Page
def User_Signup(request):
    if request.method == "POST":
        form =  SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratutions!! You have become an author.")
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

# Login Page
def User_Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully !! ")
                    return HttpResponseRedirect('/Dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/Dashboard/')


# Logout Page
def User_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
