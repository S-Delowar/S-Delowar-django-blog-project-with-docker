from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from Blog_Project.views import index_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),
    path('blogs/', include('Blog_App.urls')),
    path('accounts/', include('Registration_App.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
