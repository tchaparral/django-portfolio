'''Módulo para views de login Django.'''
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from users.forms import LoginForms, CadastroForms




def login(request):
    '''Responde à request para a página inicial de login.'''
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_usuario = form.cleaned_data['nome_usuario']
            senha = form.cleaned_data['senha']

        usuario = auth.authenticate(
            request,
            username=nome_usuario,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            primeiro_nome = usuario.first_name
            messages.success(request, f'Bem vindo {primeiro_nome}')
            return redirect('index')

        else:
            messages.error(request, 'Usuário inválido')
            return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def cadastro(request):
    '''Responde à request para a página inicial de cadastro.'''
    form = CadastroForms(request.POST)

    if form.is_valid():

        nome_usuario = form['nome_usuario'].value()
        email = form['email'].value()
        senha = form['senha'].value()
        nome = form['nome'].value()
        sobremone = form['sobrenome'].value()

        if User.objects.filter(username=nome_usuario).exists(): # ususario já cadastrado
            return redirect('login')

        usuario = User.objects.create_user(
            username = nome_usuario,
            email = email,
            password = senha,
            first_name = nome,
            last_name = sobremone
        )

        usuario.save()
        return redirect('login')

    return render(request, 'users/cadastro.html', {'form': form})


def logout(request):
    '''Responde à request para logout.'''
    auth.logout(request)
    return redirect('index')
