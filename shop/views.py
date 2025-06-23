from django.shortcuts import render,get_object_or_404,redirect
from . import models
from .forms import RegistrationForm,LoginForm,CommentForm
from django.contrib.auth import login,logout,authenticate

def homepage(request):
    products = models.Products.objects.all()
    return render(request,'index.html',{'prod':products})

def detail(request,id):
    product = get_object_or_404(models.Products,id = id)
    comments = models.Comment.objects.filter(product = product)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = request.user
            new_comment.save()
            return redirect('detail',id = product.id)
    else:
        comment_form = CommentForm()
    context = {
        'forms':comment_form,
        'comments':comments,
        'product':product
    }

    return render(request,'detail.html',context)

def registration(request):
    if request.method=='POST':
        forms = RegistrationForm(request.POST,request.FILES)
        if forms.is_valid():
            user = forms.save()
            login(request,user)
            return redirect('home')
    else:
        forms = RegistrationForm()
    return render(request,'user/registration.html',{'forms':forms})

def log_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method=='POST':
        forms = LoginForm(request,request.POST)   
        if forms.is_valid():
            user = forms.get_user()
            login(request,user)
            return redirect('home')
    else:
        forms = LoginForm
    return render(request,'user/login.html',{'forms':forms})

