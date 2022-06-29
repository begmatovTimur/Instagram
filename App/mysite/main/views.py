from django.shortcuts import redirect, render
from main.models import Post, Category, Comment
from main.post_form import PostForm
from main.user_form import SignUpForm
from main.login_form import LoginForm
from main.comment_form import CommentForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import datetime


def index(request):
    posts = Post.objects.all()
    search_posts = request.GET.get("search")
    if search_posts:
        posts = Post.objects.filter(Q(title__icontains=search_posts) and Q(text__icontains=search_posts))
    categories = Category.objects.all()

    return render(request, "main/index.html", {'posts': posts, 'categories': categories})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post__pk=pk, parent_comment__isnull=True)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "main/post_detail.html", {'post': post, 'comments': comments})


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, "main/category_detail.html", {'category': category})


def add(request):
    print(request.POST, request.FILES)
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "main/add.html", {'form': form})


def register(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "main/register.html", {'form': form})


def log_in(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
    
    return  render(request,"main/login.html", {'form': form})


def log_out(request):
    logout(request) 
    return redirect('')


def direct(request):
    return render(request, "main/direct.html")


def acc(request):
    return render(request, "main/account.html")


def add_comment(request):
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "main/add_comment.html", {'form': form})


def action(request):
    return render(request, "main/action.html")