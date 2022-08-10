from django.shortcuts import render, redirect
from accounts.models import Profile, Post
from App1.models import Pokemon
from accounts.forms import NuevoUsuarioForm, UserEditForm,  UpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.views.generic import DetailView

from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.


def registra_usuario(request):
    
    if request.method == "POST":
        form = NuevoUsuarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]

            user= form.save(commit=False)
            profile= Profile(user=user)
            user.save()
            profile.save()
            

            return render(request,'App1/inicio.html', {"mensaje": f"Se ha creado el usuario: {username}"})

    else:
        form = NuevoUsuarioForm()

    return render (request,'accounts/registra_usuario.html', {'form':form})
		
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":

        form = UserEditForm(request.POST)
        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["emial"]
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']

            usuario.save()

            return render(request, 'App1/inicio.html')

    else:
        form= UserEditForm()

    return render(request, 'accounts/editar_usuario.html', {'form': form})

def login_request(request):

    if request.method == "POST":
      
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
          
            if user is not None:
                login(request,user)
                
                return render(request,"App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request, "accounts/login.html", {"mensaje": "Usuario o clave incorrectos"})

        else:
           
            return render (request,"accounts/login.html", {"mensaje":"Error,forumlario erroneo"})

    form = AuthenticationForm()

    return render(request, "accounts/login.html", {'form':form})

def logout_request(request):
    
    logout(request)

    return render(request,"App1/inicio.html")

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado')
            return render(request,"App1/inicio.html")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def profile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except User.DoesNotExist:
        user = None
        profile = None

    return render(request,'accounts/profile.html', {'user':user, 'profile':profile})


class ArticleDetailView(DetailView):
    model = Post
    template_name= 'post_details.html'