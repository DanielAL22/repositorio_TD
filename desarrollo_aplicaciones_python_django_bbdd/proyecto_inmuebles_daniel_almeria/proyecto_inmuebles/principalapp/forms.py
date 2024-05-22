from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, TipoInmueble, Comuna, Region, ImagenInmueble


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'rut', 'direccion', 'telefono', 'email', 'tipo_usuario', 'password1', 'password2']
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'direccion', 'telefono', 'email', 'tipo_usuario']
        
        
class AddPropertyForm(forms.Form):
    # usuario: Usuario
    tipo_inmueble = forms.ModelChoiceField(queryset=TipoInmueble.objects.all(), empty_label='', label='Tipo de inmueble')
    nombre = forms.CharField(max_length=100, label='Nombre de la propiedad')
    descripcion = forms.CharField(max_length=200)
    m2_construidos = forms.IntegerField(label='Metros cuadrados construidos')
    m2_totales = forms.IntegerField(label='Metros cuadrados totales')
    n_estacionamientos = forms.IntegerField(label='Número de estacionamientos')
    n_habitaciones = forms.IntegerField(label='Número de habitaciones')
    n_baños = forms.IntegerField(label='Número de baños')
    nombre_direccion = forms.CharField(max_length=100, label='Dirección')
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='')
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label='')
    precio = forms.IntegerField()
    
class ImagenInmuebleForm(forms.ModelForm):
    class Meta:
        model = ImagenInmueble
        fields = ['imagen']

class UpdatePropertyForm(forms.Form):
    tipo_inmueble = forms.ModelChoiceField(queryset=TipoInmueble.objects.all(), empty_label='', label='Tipo de inmueble')
    nombre = forms.CharField(max_length=100, label='Nombre de la propiedad')
    descripcion = forms.CharField(max_length=200)
    m2_construidos = forms.IntegerField(label='Metros cuadrados construidos')
    m2_totales = forms.IntegerField(label='Metros cuadrados totales')
    n_estacionamientos = forms.IntegerField(label='Número de estacionamientos')
    n_habitaciones = forms.IntegerField(label='Número de habitaciones')
    n_baños = forms.IntegerField(label='Número de baños')
    nombre_direccion = forms.CharField(max_length=100, label='Dirección')
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='')
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label='')
    precio = forms.IntegerField()
    disponible = forms.BooleanField(label='Disponible', required=False, initial=True) #por si el usuario quiere disponer de la propiedad temporalmente
    
    
class SearchPropertiesForm(forms.Form):
    tipo_inmueble = forms.ModelChoiceField(queryset=TipoInmueble.objects.all(), empty_label='Todos', label='Tipo de inmueble', required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='Todas', label='Región', required=False)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label='Todas', label='Comuna', required=False)
    disponible = forms.BooleanField(label='Mostrar solo propiedades disponibles', required=False, initial=True)
    
    
# class SearchPropertiesForm(forms.Form):
#     TIPOS_INMUEBLE_CHOICES = [
#         ('', 'Todos'),  # Opción "Todos" como una opción real y seleccionada por defecto
#     ] + [(tipo_inmueble.id, tipo_inmueble) for tipo_inmueble in TipoInmueble.objects.all()]

#     REGION_CHOICES = [
#         ('', 'Todas'),  # Opción "Todas" como una opción real y seleccionada por defecto
#     ] + [(region.id, region.nombre) for region in Region.objects.all()]

#     COMUNA_CHOICES = [
#         ('', 'Todas'),  # Opción "Todas" como una opción real y seleccionada por defecto
#     ] + [(comuna.id, comuna.nombre) for comuna in Comuna.objects.all()]

#     tipo_inmueble = forms.ChoiceField(choices=TIPOS_INMUEBLE_CHOICES, label='Tipo de inmueble', initial='', required=False)
#     region = forms.ChoiceField(choices=REGION_CHOICES, label='Región', initial='', required=False)
#     comuna = forms.ChoiceField(choices=COMUNA_CHOICES, label='Comuna', initial='', required=False)
#     disponible = forms.BooleanField(label='Mostrar solo propiedades disponibles', required=False, initial=True)

    
