from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ConsultaForm, PacienteRegisterForm
from .models import Consulta, User


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
                return redirect("home_paciente")
            elif user.tipo_usuario == User.FUNCIONARIO:
                return redirect("home_funcionario")
            elif user.tipo_usuario == User.ADMIN:
                return redirect("home_admin")
        else:
            messages.error(request, "CPF ou senha inválidos!")

    return render(request, "base/login.html")


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

    return render(request, "base/register.html", {"form": form})


@login_required
def home_paciente_view(request):
    if request.user.tipo_usuario != User.PACIENTE:
        messages.error(request, "Acesso negado.")
        return redirect("login")
    return render(request, "paciente/home_paciente.html")


@login_required
def home_funcionario_view(request):
    if request.user.tipo_usuario != User.FUNCIONARIO:
        messages.error(request, "Acesso negado.")
        return redirect("login")
    return render(request, "funcionario/home_funcionario.html")


@login_required
def home_admin_view(request):
    if request.user.tipo_usuario != User.ADMIN:
        messages.error(request, "Acesso negado.")
        return redirect("login")
    return render(request, "admin/home_admin.html")


def logout_view(request):
    return render(request, "base/login.html")


@login_required
def agendar_consulta_view(request):
    if request.user.tipo_usuario != User.PACIENTE:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    paciente = request.user.paciente  # pega o paciente logado

    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.save()
            messages.success(request, "Consulta agendada com sucesso!")
            return redirect("home_paciente")
    else:
        form = ConsultaForm()

    return render(request, "paciente/agendar_consulta.html", {"form": form})


@login_required
def minhas_consultas_view(request):
    if request.user.tipo_usuario != User.PACIENTE:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    paciente = request.user.paciente  # pega o paciente logado
    consultas = Consulta.objects.filter(paciente=paciente).order_by("data", "hora")  # apenas as dele

    return render(request, "paciente/minhas_consultas.html", {"consultas": consultas})


@login_required
def consultas_disponiveis_view(request):
    if request.user.tipo_usuario != User.FUNCIONARIO:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    funcionario = request.user.funcionario  # pega o funcionário logado
    consultas_disponiveis = Consulta.objects.filter(funcionario__isnull=True).order_by("data", "hora")

    return render(request, "funcionario/consultas_disponiveis.html", {"consultas": consultas_disponiveis})


@login_required
def pegar_consulta_view(request, consulta_id):
    if request.user.tipo_usuario != User.FUNCIONARIO:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    funcionario = request.user.funcionario
    consulta = get_object_or_404(Consulta, id=consulta_id)

    if consulta.funcionario is not None:
        messages.error(request, "Essa consulta já foi atribuída a outro funcionário.")
    else:
        consulta.funcionario = funcionario
        consulta.save()
        messages.success(request, "Você pegou a consulta com sucesso!")

    return redirect("consultas_disponiveis")


@login_required
def minhas_consultas_funcionario_view(request):
    if request.user.tipo_usuario != User.FUNCIONARIO:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    funcionario = request.user.funcionario
    consultas = Consulta.objects.filter(funcionario=funcionario, concluida=False).order_by("data", "hora")

    return render(request, "funcionario/minhas_consultas_funcionario.html", {"consultas": consultas})


@login_required
def concluir_consulta_view(request, consulta_id):
    if request.user.tipo_usuario != User.FUNCIONARIO:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    funcionario = request.user.funcionario
    consulta = get_object_or_404(Consulta, id=consulta_id, funcionario=funcionario)

    consulta.concluida = True
    consulta.save()
    messages.success(request, "Consulta concluída com sucesso!")

    return redirect("minhas_consultas_funcionario")


@login_required
def consultas_concluidas_funcionario_view(request):
    if request.user.tipo_usuario != User.FUNCIONARIO:
        messages.error(request, "Acesso negado.")
        return redirect("login")

    funcionario = request.user.funcionario
    consultas = Consulta.objects.filter(funcionario=funcionario, concluida=True).order_by("-data", "-hora")

    return render(request, "funcionario/consultas_concluidas_funcionario.html", {"consultas": consultas})
