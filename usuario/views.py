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

            return redirect("/usuario/login" , )
    else:
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


class Dispositivo:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def receber_coordenadas(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    # dispositivo = Dispositivo(latitude, longitude)

    # import geocoder
    # from haversine import haversine, Unit
    # notebook = geocoder.ip('me')

    # latitude_notebook = notebook.latlng[0]
    # longitude_notebook = notebook.latlng[1]

    # coord_dispositivo = (dispositivo.latitude , dispositivo.longitude)


    # # distancia_metros = haversine((latitude_notebook,longitude_notebook), coord_dispositivo, unit=Unit.METERS)

    # print(f"Latitude: {notebook.latlng[0]}, Longitude: {notebook.latlng[1]}")
    # print(f"Latitude: {dispositivo.latitude},Longitude: {dispositivo.longitude}")

    # # print(f"Distância entre os pontos: {distancia_metros:.2f} metros")

    # # if distancia_metros > 100:

    # #     print("ELE ESTA FORA DO RAIO")

    # # else:
    # #     print("TUDO CERTO")

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    return JsonResponse({
        "lat": latitude,
        "long": longitude
    })



