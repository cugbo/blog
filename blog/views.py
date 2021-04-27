from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailsView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name ='post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect ('/templates/home.html')
        else:
            request.session ['invalid_user'] = 1
            return render(request, 'login.html', {'login'.form})

def logout_view(request):
    logout(request)
    return redirect ('/templates/login.html')


def register_view(request):
    form = Register.Form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        password = form.cleaned_data.get('password2')
    try:
       user.object.create_user (username, email, password)
    except:
        user = None
    if user != None
        login(request, user)
        return redirect ('/templates/base.html')
    else:
        request.session['register_error'] = 1
    return render (request, 'registration.html', {'register'.form})
    