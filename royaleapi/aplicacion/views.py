from django.shortcuts import render, redirect
from requests.api import get
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from aplicacion import serializers
from .models import Jugador
from .forms import Buscar
import requests

headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI0M2I0ZGZmLWY5ODQtNDE0OS05ZWI4LTU2OGQ2ZTNkZTA3NSIsImlhdCI6MTYzOTU0MjAyNSwic3ViIjoiZGV2ZWxvcGVyLzMwMjZhMzQyLTAyYjItNzdjZi04ODllLWMyNDc2NTE3MGI3ZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3OS4xNDguNjkuMjI0Il0sInR5cGUiOiJjbGllbnQifV19.-rUbj6cgAxQsH8wRDp0L260cM_z-JzqZm0VhsLLYpA6SNcnMT4t1IjHiT7_MXSSsXEsRfT89_CkidlKBJzB5ng',
    'Accept': 'application/json'
}

def inicio(request):
    return render(request, "paginas/inicio.html")

def perfilinfo(request, usuario):
    try:
        url = 'https://api.clashroyale.com/v1/players/%23' + str(usuario)
        usuarioInfo = requests.get(url, headers=headers).json()

        return render(request, "paginas/perfilinfo.html", {'nombre': usuarioInfo['name'],
                                                                'tag': usuarioInfo['tag'],
                                                                'nivel': usuarioInfo['expLevel'],
                                                                'arena': usuarioInfo['arena']['name'],
                                                                'wins': usuarioInfo['wins'],
                                                                'losses': usuarioInfo['losses'],
                                                                'threeCrownWins': usuarioInfo['threeCrownWins'],
                                                                'warDayWins': usuarioInfo['warDayWins'],
                                                                'challengeMaxWins': usuarioInfo['challengeMaxWins'],
                                                                'totalDonations': usuarioInfo['totalDonations'],
                                                                'clan': usuarioInfo['clan']})
    except:
        return render(request, 'paginas/noencontrado.html')


def jugadores(request):
    jugadores = Jugador.objects.all()
    
    return render(request, "paginas/jugadores.html", {'jugadores': jugadores})

def buscar(request):
    if request.method == 'POST':
        form = Buscar(request.POST)
        texto = request.POST['buscar']
        
        if form.is_valid():
            return redirect('perfilinfo', usuario=texto)
		
    else:
        form = Buscar()

    context = {'form': form}

    return render(request, "paginas/buscar.html", context)

class JugadorAPI(APIView):
    serializer_class = serializers.APISerializer

    def get(self, request, format=None):
        jugador = Jugador.objects.all()
        serializer = serializers.APISerializer(jugador, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            tagSerializer = serializer.validated_data.get('tag')
            jugador = Jugador.objects.all().filter(tag=tagSerializer)
            serializer = serializers.APISerializer(jugador, many=True)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)