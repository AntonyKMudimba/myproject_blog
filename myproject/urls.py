
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
