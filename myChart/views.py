import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class baseView(TemplateView):
    template_name = 'base.html'
    
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
    
    if request.method == 'POST':         
         email = request.POST.get('email')
         password = request.POST.get('password')
         
         user = authenticate(email = email, password = password)
         if user is not None:
             login(request, user)
             return redirect('base')
         else:
            messages.error(request, 'Incorrect Email or Password')
    
    context = {}
    return render(request, 'login.html', context)

def signUpView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        approve = True
        
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        regex_num = re.compile('[0-9]')
        regex_upper = re.compile('[A-Z]')
        
        if (len(password) < 8 or regex.search(password) == None or regex_num.search(password) == None or regex_upper.search(password) == None):
            messages.error(request, 'Password must at least contains 8 characters (Including at least 1 special character, 1 number and 1 uppercase letter)')
            approve = False
            
        if (len(username) < 8):
            messages.error(request, 'Username must at least contains 8 characters')
        
        getAllUsers_username = User.objects.filter(username=username)
        if getAllUsers_username: 
            messages.error('Username already exists')
            approve = False
            
        if (password != confirm_password):
            messages.error("Password doesn't match")
            approve = False
        
        if approve == True:
            new_user = User.objects.create_user(username = username, email = email, password = password)
            new_user.save()
            login(request, new_user)
            return redirect('base')
    
    context = {}
    return render(request, 'register.html', context)
        
        
    
    
     
      

    
         