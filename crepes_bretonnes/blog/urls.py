"""crepes_bretonnes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings
# On import les vues de Django, avec un nom spécifique
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accueil', views.home),
#    path('article/<id_article>', views.view_article, name='afficher_article'),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),

    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/',views.addition),
    path('mapping', views.mapping),
    path('photos', views.view_photos),

    path('',views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),

    path('contact/', views.nouveau_contact, name='contact'),
    path('voir_contacts/', views.voir_contacts, name='voir_contacts'),

#    path(r'connexion', views.connexion, name='connexion'),

    path(r'deconnexion', views.deconnexion, name='deconnexion'),
    path('connexion', auth_views.login, {'template_name': 'auth/connexion.html'})


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

