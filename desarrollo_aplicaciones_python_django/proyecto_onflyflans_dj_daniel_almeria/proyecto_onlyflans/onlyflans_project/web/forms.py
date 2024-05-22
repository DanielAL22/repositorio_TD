from django import forms
from .models import ContactForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    #debe contener los atributos necesarios para poder recibir los datos necesarios en el modelo ContactForm
    #contact_form_uuid no necesita ser declarado en el form
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")
    
    
class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre del cliente',
            'message': 'Mensaje',
        }


class CustomUserCreationForm(UserCreationForm):
    #heredamos los atributos de UserCreationForm, incluye nombre de usuario, contraseña y verificación de contraseña, el resto se agreagan aquí
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    