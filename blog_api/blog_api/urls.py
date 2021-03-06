from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace = "posts")),
    path('comments/', include('comments.urls', namespace = 'comments')),
    path('users/', include('users.urls', namespace = 'users')),
]


# to serve the static files during developement
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)