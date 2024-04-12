from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Este es el home de la aplicación</h1>")

def about(request):
    return HttpResponse("<h1>Este es el about de la aplicación</h1>")

def contact(request):
    return HttpResponse("""<h1>Este es el contact de la aplicación</h1>
                            <form action="mailto:destinatario@example.com" method="post" enctype="text/plain">
                                <label for="nombre">Nombre:</label>
                                <input type="text" id="nombre" name="nombre" required><br><br>
                                
                                <label for="email">Email:</label>
                                <input type="email" id="email" name="email" required><br><br>
                                
                                <label for="mensaje">Mensaje:</label><br>
                                <textarea id="mensaje" name="mensaje" rows="4" cols="50" required></textarea><br><br>
                                
                                <input type="submit" value="Enviar">
                            </form>
                        """)