from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pages.urls')),
    path('cars/', include('Cars.urls')),
    path('accounts/', include('Accounts.urls')),
    path('contacts/', include('Contacts.urls')),
    path('socialaccounts/',include('allauth.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)