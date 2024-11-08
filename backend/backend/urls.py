"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from home import views as views_home
from locality import views as views_locality
from source import views as views_source
import authentication.views
from django.contrib.auth.views import LoginView, LogoutView
from maintenance import views as views_maintenance
from remplacement import views as views_remplacement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views_home.home, name='home'),
    path('locality/', views_locality.locality, name='locality'),
    path('locality/<int:id>/', views_locality.locality_update, name='locality-update'),
    path('source/', views_source.source, name='source'),
    path('source/<int:id>/', views_source.source_update, name='source-update'),
    path('maintenance/', views_maintenance.maintenance, name='maintenance'),
    path('maintenance/<int:id>/', views_maintenance.maintenance_update, name='maintenance-update'),
    path('remplacement/', views_remplacement.remplacement, name='remplacement'),
    path('remplacement/<int:id>/', views_remplacement.remplacement_update, name='remplacement-update'),
    #section gérant l'authentification et la création des comptes utilisateurs
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'
        ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
]
