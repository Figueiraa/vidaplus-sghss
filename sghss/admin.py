from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Consulta, Funcionario, Paciente, User


# =========================
# Custom User Admin
# =========================
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("cpf", "name", "tipo_usuario", "is_staff", "is_active")
    list_filter = ("tipo_usuario", "is_staff", "is_active")
    search_fields = ("cpf", "name")
    ordering = ("cpf",)
    fieldsets = (
        (None, {"fields": ("cpf", "name", "password", "tipo_usuario")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "cpf",
                    "name",
                    "tipo_usuario",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


# =========================
# Paciente Admin
# =========================
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("user", "cpf", "nome")
    search_fields = ("user__cpf", "user__name")
    list_filter = ("user__is_active",)

    def cpf(self, obj):
        return obj.user.cpf

    cpf.admin_order_field = "user__cpf"

    def nome(self, obj):
        return obj.user.name

    nome.admin_order_field = "user__name"


# =========================
# Funcionario Admin
# =========================
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("user", "nome", "cpf", "cargo", "ativo")
    search_fields = ("user__cpf", "user__name", "cargo")
    list_filter = ("cargo", "user__is_active")

    def cpf(self, obj):
        return obj.user.cpf

    cpf.admin_order_field = "user__cpf"

    def nome(self, obj):
        return obj.user.name

    nome.admin_order_field = "user__name"

    def ativo(self, obj):
        return obj.user.is_active

    ativo.boolean = True
    ativo.admin_order_field = "user__is_active"


# =========================
# Consulta Admin
# =========================
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        "paciente_nome",
        "funcionario_nome",
        "data",
        "hora",
        "concluida",
    )
    search_fields = ("paciente__user__name", "funcionario__user__name", "descricao")
    list_filter = ("concluida", "data")
    ordering = ("-data", "hora")

    def paciente_nome(self, obj):
        return obj.paciente.user.name

    paciente_nome.admin_order_field = "paciente__user__name"

    def funcionario_nome(self, obj):
        if obj.funcionario:
            return obj.funcionario.user.name
        return "-"

    funcionario_nome.admin_order_field = "funcionario__user__name"
