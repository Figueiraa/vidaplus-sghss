"""
URL configuration for vidaplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from sghss import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_view, name="login"),
    path("home_paciente/", views.home_paciente_view, name="home_paciente"),
    path("home_funcionario/", views.home_funcionario_view, name="home_funcionario"),
    path("home_admin/", views.home_admin_view, name="home_admin"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("agendar-consulta/", views.agendar_consulta_view, name="agendar_consulta"),
    path("minhas-consultas/", views.minhas_consultas_view, name="minhas_consultas"),
    path("consultas-disponiveis/", views.consultas_disponiveis_view, name="consultas_disponiveis"),
    path("pegar-consulta/<int:consulta_id>/", views.pegar_consulta_view, name="pegar_consulta"),
    path("minhas-consultas-funcionario/", views.minhas_consultas_funcionario_view, name="minhas_consultas_funcionario"),
    path("concluir-consulta/<int:consulta_id>/", views.concluir_consulta_view, name="concluir_consulta"),
    path(
        "consultas-concluidas-funcionario/",
        views.consultas_concluidas_funcionario_view,
        name="consultas_concluidas_funcionario",
    ),
]
