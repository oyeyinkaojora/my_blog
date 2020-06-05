from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.views.generic.detail import DetailView
from .forms import PostCreationForm,CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }        
    return render(request,'blog/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context = {}         
    return render(request,'blog/login.html',context) 


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')


def postCreate(request):
    form = PostCreationForm()
    if request.method =='POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }        
    return render(request,'blog/post_creation.html',context)


class postDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

@login_required
def postUpdate(request,pk):
    posts = Post.objects.get(id=pk)
    form = PostCreationForm(instance=posts)
    if request.method =='POST':
        form = PostCreationForm(request.POST,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }        
    return render(request,'blog/post_update.html',context)

@login_required
def postDelete(request,pk):
    posts = Post.objects.get(id = pk)
    posts.delete()
    return redirect('home')    




