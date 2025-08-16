from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, cpf, name, password=None, **extra_fields):
        if not cpf:
            raise ValueError("O CPF deve ser informado")
        if not name:
            raise ValueError("O nome deve ser informado")
        cpf = str(cpf)
        user = self.model(cpf=cpf, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, name, password=None, **extra_fields):
        extra_fields.setdefault("tipo_usuario", User.ADMIN)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(cpf, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    PACIENTE = "paciente"
    FUNCIONARIO = "funcionario"
    ADMIN = "admin"

    USER_TYPE_CHOICES = [
        (PACIENTE, "Paciente"),
        (FUNCIONARIO, "Funcionário"),
        (ADMIN, "Administrador"),
    ]

    cpf = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=150)
    tipo_usuario = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return f"{self.cpf} ({self.tipo_usuario})"


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
