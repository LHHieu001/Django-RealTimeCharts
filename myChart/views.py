import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import VoteForm

@login_required
def baseView(request):
    
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('base')
    else:
        form = VoteForm()
        
    userVote = voter.objects.filter(user=request.user).first()
    if userVote:
        voted_for = dict(voter.candi.choices)[userVote.vote]
    else:
        voted_for = None
    context = {
        'form' : form,
        'current_user': request.user,
        'userVote' : userVote,
        'voted_for' : voted_for
    }
    return render(request, 'base.html', context)
# class signInView(FormView):
#     template_name = 'login.html'
#     success_url = reverse_lazy('base')
    
#     def post(self):
#         form = AuthenticationForm(data=self.request.POST)
#         if form.is_valid():
#             return redirect(self.get_success_url())
        
            
# class signUpView(FormView):
#     template_name = 'register.html'
#     success_url = reverse_lazy('base')
    
#     def post(self):
#         form = UserCreationForm(self.request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(self.get_success_url())

def signInView(request):
    
    if request.user.is_authenticated:
        return redirect('base')
    
    if request.method == 'POST':         
         email = request.POST.get('email')
         password = request.POST.get('password')
         
         user = authenticate(username = email, password = password)
         if user is not None:
             login(request, user)
             return redirect('base')
         else:
            messages.error(request, 'Incorrect Email or Password')
    

    context = {}
    return render(request, 'login.html', context)

def signUpView(request):
    
    if request.user.is_authenticated:
        return redirect('base')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        approve = True
        
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
        regex_num = re.compile('[0-9]')
        regex_upper = re.compile('[A-Z]')
        
        if (len(password) < 8 or regex.search(password) == None or regex_num.search(password) == None or regex_upper.search(password) == None):
            messages.error(request, 'Password must at least contains 8 characters (Including at least 1 special character, 1 number and 1 uppercase letter)')
            approve = False
        
        getAllUsers_username = User.objects.filter(username=email)
        if getAllUsers_username: 
            messages.error(request, 'Email already exists')
            approve = False
            
        if (password != confirm_password):
            messages.error(request, "Password doesn't match")
            approve = False
        
        if approve == True:
            new_user = User.objects.create_user(username = email, password = password)
            new_user.save()
            login(request, new_user)
            return redirect('base')
    
    context = {}
    return render(request, 'register.html', context)

def chartView(request):
    context = {}
    return render(request, 'chart.html', context)

@login_required
def signOutView(request):
    logout(request)
    return redirect('signin')
    
        
        
    
    
     
      

    
         