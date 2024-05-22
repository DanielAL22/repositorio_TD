from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField() #campo UUID o Identificador Único Universal es un estándar de generación de identificadores únicos
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField() #ImageField(upload_to = 'web/static/img/') al parecer no se hace si esta configurado en el settings
    slug = models.SlugField() #nombre corto de url
    is_private = models.BooleanField() #definir si el flan es privado o no
    
    
class ContactForm(models.Model):
    #permitirá crear distintos ContactForm que podrán ser creados en la web y presentados a través del panel de administración de Django
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False) # uuid.uuid4 permitirá definir automáticamente un UUID en su versión 4(al azar) cada vez que se genere un nuevo registro del modelo ContactForm
    customer_email= models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
