from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import LoginForm , RegisterForm
from django.contrib.auth.hashers import check_password , make_password 


def register(request):


    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome'].strip()
            telefone = form.cleaned_data['telefone'].strip()
            email = form.cleaned_data['email'].strip()
            senha = form.cleaned_data['senha']
            

            if Usuario.objects.filter(email=email).exists():
                messages.error(request, "Este e-mail já está em uso.")
                
                return render(request, "register.html", {"form": form})

            usuario = Usuario(nome=nome, telefone=telefone, email=email, senha=make_password(senha))

            usuario.save()

            request.session['usuario_id'] = usuario.userID

            login(request)

            return redirect("/usuario/login" , {"form": form})
        else:
            messages.error(request, "Nenhum campo pode ser vazio.")
            form = RegisterForm()

    else:
        messages.error(request, "Tipo de requisição inválido.")
        form = RegisterForm()

    return render(request,'register.html', {"form": form})

def login(request):

    # if request.session.get('usuario_id'):
    #     return redirect('/usuario/home')

    if request.method == "POST":

        form = LoginForm(request.POST)


        if form.is_valid():


            email = form.cleaned_data['email'].strip()
            senha = form.cleaned_data['senha']

            try:
                usuario = Usuario.objects.get(email=email)

                if check_password(senha, usuario.senha): 

                    request.session['usuario_id'] = usuario.userID

                    return redirect('/usuario/home')
                
                else:

                    messages.error(request, "Senha incorreta.")

            except Usuario.DoesNotExist:

                messages.error(request, "Usuário não encontrado.")
    else:

        form = LoginForm()
        
    return render(request, "login.html", {"form": form})


def home(request):

    return render(request, "home.html")

from django.http import JsonResponse


# class Dispositivo:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
import json
def receber_coordenadas(request):
    if request.method == "GET":
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if latitude and longitude:
            print(f"[GET] Latitude: {latitude}, Longitude: {longitude}")
            return JsonResponse({
                "lat": latitude,
                "long": longitude
            })
        else:
            return render(request, 'receber_coordenadas.html')

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            print(f"[POST] Latitude: {latitude}, Longitude: {longitude}")

            return JsonResponse({
                "lat": latitude,
                "long": longitude
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

    return JsonResponse({"error": "Método não permitido"}, status=405)



