from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    nome = forms.CharField(label="nome")
    telefone = forms.CharField(label="telefone")
    email = forms.EmailField(label="mail")
    senha = forms.CharField(label="senha", widget=forms.PasswordInput)