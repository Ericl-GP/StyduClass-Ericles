from django import forms
from socialapp.models import Avalia, Postagem,Perfil, Telefone,Perfil_post
from django import forms



class AvaliaForms(forms.ModelForm):
    class Meta:
        model = Avalia
        fields ="__all__"


class PostagemForms(forms.ModelForm):
    class Meta:
        model = Postagem
        fields ="__all__"


class PerfilForms(forms.ModelForm):
    class Meta:
        model = Perfil
        fields ="__all__"


class TelefoneForms(forms.ModelForm):
    class Meta:
        model = Telefone
        fields ="__all__"


class PerfilPostForms(forms.ModelForm):
    class Meta:
        model = Perfil_post
        fields ="__all__"



