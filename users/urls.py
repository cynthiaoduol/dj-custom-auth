from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
     path('hospitals/register',views.HospitalRegistrationView.as_view(),name='register'),
    path('hospitals/login',views.HospitalLoginView.as_view(),name='login'),
   

]

if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)