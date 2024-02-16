# taskmanager2


!!!!! IT WILL BE MORE UPDATES !!!!!




1. cd taskamanger2 
2. Deschidem proiectul (django-admin startproject taskmanager2)
3. django-admin startapp main2
4. Dupa in [settings.py](http://settings.py) adaugam aplicatia in INSTALLED_APPS, ca in next example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main2',
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
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('room/<str:pk>/', views.room, name = 'room')
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

1. python3 [manage.py](http://manage.py) makemigrations
2. python3 [manage.py](http://manage.py) migrate
3. python3 [manage.py](http://manage.py) createsuperuser (deja adaugam userul si parola)
4. python3 [manage.py](http://manage.py) runserver
5. deja deschidem in [localhost](http://localhost) si intram in /admin (ex: http://127.0.0.1:8000/admin/) si ne logam

6. folderul templates → in [settings.py](http://settings.py) la sectiunea ,,TEMPLATES” in rindul 2 cu DIRS modificam: 'DIRS': [BASE_DIR/'templates'],

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

1. Create dir → main2 → templates
2. In templates creem → main2 (cu numele aplicatiei)
3. In main2 recent creat, facem urmatoarele files: home.html, main.html, navbar.html, room.html
4. Punem aceste 4 fileuri in templates si in main2 din templates
5. python3 [manage.py](http://manage.py) runserver