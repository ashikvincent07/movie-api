from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import MovieSerializer, UserSerializer
from api.models import Movie

from django.contrib.auth.models import User
from rest_framework import authentication, permissions


class MovieCreateListView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = MovieSerializer(data=data)

        if serializer_instance.is_valid():

            Movie.objects.create(**data)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)
        
    
    def get(self, request, *args, **kwargs):

        qs = Movie.objects.all()

        serializer_instance = MovieSerializer(qs, many=True)

        return Response(data=serializer_instance.data)

        


class MovieRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = Movie.objects.get(id=id)

        serializer_instance = MovieSerializer(qs)

        return Response(data=serializer_instance.data)
    


    def put(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        serializer_instance = MovieSerializer(data=request.data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Movie.objects.filter(id=id).update(**cleaned_data)

            return Response(data=serializer_instance.data)
        

        else:

            return Response(data=serializer_instance.errors)
        


    def delete(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        return Response({"message" : "Deleted"})



class SignUpView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = UserSerializer(data=data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_user(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        