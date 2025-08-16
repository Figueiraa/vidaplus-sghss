from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Paciente, User


class PacienteRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=150)
    cpf = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ["name", "cpf", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data["name"]
        user.tipo_usuario = User.PACIENTE
        if commit:
            user.save()
            Paciente.objects.create(user=user)
        return user
