from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES = [
        ('Docente', 'Docente'),
        ('Discente', 'Discente')
    ]

    username = forms.CharField(label='Usuario:')
    email = forms.EmailField(label='E-mail:')
    last_name = forms.CharField(label='Matricula:')
    first_name = forms.ChoiceField(
        label='Status:',
        choices=FIRST_NAME_CHOICES,
        widget=forms.Select(attrs={'class': 'custom-select'}),
        initial='Discente'
    )

    # Campos de senha personalizados
    password1 = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirme a senha:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']
