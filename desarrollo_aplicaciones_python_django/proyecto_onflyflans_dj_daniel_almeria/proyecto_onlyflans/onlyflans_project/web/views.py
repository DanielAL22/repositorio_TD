from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm, CustomUserCreationForm



# Create your views here.
def index(request):
    
    #obtenemos la lista de flanes
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    my_dict = {
        "lista_flanes" : flanes,
        "lista_flanes_privados": flanes_privados,
        "lista_flanes_publicos": flanes_publicos
    }
    
    return render(request=request, template_name= "pages/index.html", context=my_dict)

def about(request):
    return render(request=request, template_name= "pages/about.html", context={})


@login_required
def welcome(request):
        #obtenemos la lista de flanes
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    my_dict = {
        "lista_flanes" : flanes,
        "lista_flanes_privados": flanes_privados,
        "lista_flanes_publicos": flanes_publicos
    }
    return render(request=request, template_name= "pages/welcome.html", context=my_dict)


def contact(request):
    """debemos realizar las validaciones necesarias para validar el método de la solicitud(GET o POST), 
    obtener su data, pasarle esa data a nuestro formulario, validarlo y luego redirigir al usuario a otra ruta."""
    
    # Verifica si la solicitud es de tipo POST (envio)
    if request.method == 'POST':
        # Crea una instancia del formulario ContactFormForm con los datos de la solicitud POST
        form = ContactFormModelForm(request.POST)
        # Verifica si el formulario es válido
        if form.is_valid():
            #crear un nuevo registro usando los datos del formulario a través de form.cleaned_data
            form.save()
            #contact_form = ContactFormModelForm.objects.create(**form.cleaned_data)
            
            
            
            # Redirige al usuario a la ruta '/' en caso de que el formulario sea válido
            return HttpResponseRedirect('/exito')
        
    else:
        # Crea una instancia vacía del formulario ContactFormForm si la solicitud no es de tipo POST, osea si es GET (solicitud)
        form = ContactFormModelForm()
    
    # Renderiza la plantilla 'contact.html' y pasa el formulario 'form' como contexto
    return render(request=request, template_name="pages/contact.html", context={'form': form})


def success(request):
    return render(request=request, template_name="pages/success.html", context={})


def exit(request):
    logout(request)
    return render(request=request, template_name="registration/logout.html", context={})


def register(request):
    # data = {"form": CustomUserCreationForm()}
    
    if request.method == "POST":
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            #logeo automático al registrarse
            #authenticate devuelve un objeto User si las credenciales son correctas
            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            #hacemos el login
            login(request, user)
            
            return HttpResponseRedirect('/bienvenido')
        
    else:
        # Crea una instancia vacía del formulario ContactFormForm si la solicitud no es de tipo POST, osea si es GET (solicitud)
        user_creation_form = CustomUserCreationForm()
    
    return render(request=request, template_name="registration/register.html", context={'form': user_creation_form})