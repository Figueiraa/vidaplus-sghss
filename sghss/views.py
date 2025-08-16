from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import PacienteRegisterForm
from .models import User


def login_view(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")

        # Autentica usando o CPF
        user = authenticate(request, cpf=cpf, password=password)

        if user is not None:
            login(request, user)
            # Redireciona de acordo com o tipo de usuário
            if user.tipo_usuario == User.PACIENTE:
                return redirect("home")
            elif user.tipo_usuario == User.FUNCIONARIO:
                return redirect("home")
            elif user.tipo_usuario == User.ADMIN:
                return redirect("home")
        else:
            messages.error(request, "CPF ou senha inválidos!")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        form = PacienteRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect("login")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = PacienteRegisterForm()

    return render(request, "register.html", {"form": form})


def home_view(request):
    return render(request, "home.html")


def logout_view(request):
    return render(request, "login.html")
