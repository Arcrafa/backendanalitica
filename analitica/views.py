from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
import json


@api_view(['POST'])
def login(request):

    body_dict=json.loads(request.body.decode('utf-8'))
    username = body_dict['username']
    password = body_dict['password']
    try:

        user = User.objects.get(username=username)

    except User.DoesNotExist:
        return Response("usuario invalido")

    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return Response("contraseña invalida")

    token,create = Token.objects.get_or_create(user=user)
    print(token)
    return Response(token.key)
