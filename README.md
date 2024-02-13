# taskmanager2


!!!!! IT WILL BE MORE UPDATES !!!!!




1. cd taskamanger_2 
2. Deschidem proiectul (django-admin startproject s,,main2’’)
3. django-admin startapp app2
4. Dupa in [settings.py](http://settings.py) adaugam aplicatia in INSTALLED_APPS, ca in next example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app2',
]
```

1. To run the server run this command: python3 [manage.py](http://manage.py) runserver
2. [models.py](http://models.py) → aici se proiectează tabelele:

```python
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    Created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
```

1. Folosim fisierul [admin.py](http://admin.py) → înregistrare in DB:
    
    ```python
    from django.contrib import admin
    from.models import Room
    
    admin.site.register(Room)
    ```
    
2. [urls.py](http://urls.py) →

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main2.urls'))
]
```

1. Facem un file cu numele ,,urls.py” in folderul app2 (url-ul aplicatiei). Next in this file we will write: 

```python
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('room/<str:pk>/', views.room, room = 'room')
]
```

1. Completam fisierul [views.py](http://views.py) cu urm linii de cod:

```python
from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'main2/home.html', context)

def room(request, pk):
    rooms = None
    for i in room:
        if i['id'] == int(pk):
            room = i,
    context = {'room': room}
    return render(request,'main2/room.html', context)
```