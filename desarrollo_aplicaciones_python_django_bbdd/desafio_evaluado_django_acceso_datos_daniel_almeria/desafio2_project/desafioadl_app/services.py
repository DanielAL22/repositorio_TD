from desafioadl_app.models import Tarea, SubTarea  

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    
    #transformamos el queryset que viene con all() en una lista de objetos
    lista_tareas = list(tareas)
    lista_subtareas = list(subtareas)
    
    #return {'tareas': lista_tareas, 'subtareas': lista_subtareas}
    
    return [lista_tareas, lista_subtareas]
    


    
def imprimir_en_pantalla(array):
    for tarea in array[0]:
        print(tarea.descripcion)
        for subtarea in tarea.subtarea_set.all():
            print(f"------>{subtarea.descripcion}")
            
        # for subtarea in array[1]:
        #     if tarea.id == subtarea.tarea_id:
        #         print(f"------>{subtarea.descripcion}")
                
                

def crear_nueva_tarea(nombre_tarea):
    nueva_tarea = Tarea(descripcion=nombre_tarea)
    nueva_tarea.save()
    imprimir_en_pantalla(recupera_tareas_y_sub_tareas())
    
    
def crear_sub_tarea(nombre_subtarea, nombre_tarea):
    tarea_padre = Tarea.objects.get(descripcion=nombre_tarea)
    nueva_subtarea = SubTarea(descripcion=nombre_subtarea, tarea = tarea_padre)
    nueva_subtarea.save()
    imprimir_en_pantalla(recupera_tareas_y_sub_tareas())
    
    
def elimina_tarea(nombre_tarea):
    tarea = Tarea.objects.get(descripcion=nombre_tarea)
    tarea.eliminada = True
    tarea.save()
    # tarea.delete()
    imprimir_en_pantalla(recupera_tareas_y_sub_tareas())
    
def elimina_subtarea(nombre_subtarea):
    subtarea = Tarea.objects.get(descripcion=nombre_subtarea)
    subtarea.eliminada = True
    subtarea.save()
    # tarea.delete()
    imprimir_en_pantalla(recupera_tareas_y_sub_tareas())