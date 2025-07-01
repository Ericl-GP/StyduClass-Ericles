from django.shortcuts import render, redirect
from .forms import UsuarioForm



def new_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # substitua por uma URL válida
    else:
        form = UsuarioForm()

    return render(request, 'usuario/usuario.html', {'form': form})




