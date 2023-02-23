from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from django.urls import reverse_lazy
# from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import  Tasks
# from django.shortcuts import  render,redirect
# from .forms import Registerform,Signinform
# from django.contrib.auth.views import LoginView

# Create your views here.


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# from .forms import RegisterForm,LoginForm

# from .models import Tasks,Register,Login
# Create your views here.

class TaskList(ListView):
    model= Tasks
    context_object_name = 'task1'
    template_name = 'tasklist.html'

class TaskCreate(CreateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

class TaskUpdate(UpdateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

class TaskDelete(DeleteView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task1')
    template_name = 'taskdetail.html'


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, 'tasklist.html', {'fname': fname})

        else:
            return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully!')
    return redirect('signin')


def home(request):
    template="index.html"
    context={}
    return render(request,template,context)