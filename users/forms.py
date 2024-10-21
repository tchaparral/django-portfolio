'''Importa o módulo de formulários do Django para criação de formulários personalizados.'''
from django import forms


class LoginForms(forms.Form):
    '''Define um formulário de login personalizado usando o módulo de formulários do Django.'''
    nome_usuario = forms.CharField(
        label='Nome do usuário',
        required=True,
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'class': ' form-control',
                'placeholder': 'Digite nome de usuário'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha...'
            }
        )
    )


class CadastroForms(forms.Form):
    '''Define um formulário para cadastro personalizado usando o módulo de formulários do Django.'''
    nome = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira seu nome'
            }
        )
    )

    sobrenome = forms.CharField(
        label='Sobrenome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira seu sobrenome'
            }
        )
    )

    nome_usuario = forms.CharField(
        label='Nome de Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira o nome de usuário'
            }
        )
    )

    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira seu e-mail'
            }
        )
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha...'
            }
        )
    )

    senha_confirm = forms.CharField(
        label = 'Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha...'
            }
        )
    )

    check_termos = forms.BooleanField(
        label = 'checkbox',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'checkbox'
            }
        )
    )

    def clean_senha_confirm(self):
        '''Valida se a confirmação de senha coincide com a senha original no formulário.'''
        senha = self.cleaned_data.get('senha')
        senha_confirm = self.cleaned_data.get('senha_confirm')

        if senha and senha_confirm:
            if senha != senha_confirm:
                raise forms.ValidationError('Senhas diferentes')
            else:
                return senha_confirm
      

