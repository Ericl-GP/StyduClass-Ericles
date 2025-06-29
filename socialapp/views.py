

from django.shortcuts import render, redirect, get_object_or_404
from socialapp.forms import AvaliaForms,PostagemForms,PerfilForms, TelefoneForms, PerfilPostForms
from socialapp.models import Avalia, Postagem,Perfil, Telefone,Perfil_post
# Create your views here.
def index(request):
    postagens =Postagem.objects.all()
    return render(request, 'social/index.html', {'postagens':postagens})

def contato(request):
    return render(request, 'social/contact.html')

def home(request):
    return render(request, 'social/home.html')

def sobre(request):
    return render(request, 'social/about.html')

def postar(request):
    return render(request, 'social/post.html')

def new_avalia(request):
    avas = Avalia.objects.all()
    form = AvaliaForms()
    if request.method=='POST':
        form =AvaliaForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form= AvaliaForms()
    return render(request, 'social/new_avalia.html', {'form':form, 'avas':avas})

def editar_avalia(request, id):
    avaliado =get_object_or_404(Avalia, pk=id)
    form =AvaliaForms(instance=avaliado)
    avas =Avalia.objects.all()

    if(request.method =="POST"):
        form = AvaliaForms(request.POST, request.FILES, instance=avaliado)
        if form.is_valid():
            form.save()
            return redirect('new_avalia')
        return render(request, 'social/editar_avalia.html', {'form': form, 'avas': avas, 'avaliado':avaliado})
    else:
        return render(request, 'social/editar_avalia.html',{'form': form, 'avas': avas, 'avaliado': avaliado})



def deleta_avalia(request,id):
    avaliado = get_object_or_404(Avalia, pk=id)
    form = AvaliaForms(instance=avaliado)
    avas = Avalia.objects.all()
    if request.method == "POST":
        avaliado.delete()
        return redirect('new_avalia')
    return render(request,'social/deleta_avalia.html',{'avaliado':avaliado, 'form':form, 'avas':avas})
# Postagem
def new_post(request):
    posts = Postagem.objects.all()
    form = PostagemForms()
    if request.method=='POST':
        form =PostagemForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form= PostagemForms()
    return render(request, 'social/new_post.html', {'form':form, 'posts':posts})

def editar_post(request, id):
    post =get_object_or_404(Postagem, pk=id)
    form =PostagemForms(instance=post)
    posts =Postagem.objects.all()

    if(request.method =="POST"):
        form = PostagemForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('new_post')
        return render(request, 'social/editar_post.html', {'form': form, 'posts': posts, 'post':post})
    else:
        return render(request, 'social/editar_post.html', {'form': form, 'posts': posts, 'post':post})



def deleta_post(request,id):
    post = get_object_or_404(Postagem, pk=id)
    form = PostagemForms(instance=post)
    posts = Postagem.objects.all()
    if request.method == "POST":
        post.delete()
        return redirect('new_post')
    return render(request,'social/deleta_post.html',{'post':post, 'form':form, 'posts':posts})