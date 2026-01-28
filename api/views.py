from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import MovieSerializer
from api.models import Movie


class MovieCreateListView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = MovieSerializer(data=data)

        if serializer_instance.is_valid():

            Movie.objects.create(**data)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors,status=serializer_instance.status)
        
    
    def get(self, request, *args, **kwargs):

        qs = Movie.objects.all()

        serializer_instance = MovieSerializer(qs, many=True)

        return Response(data=serializer_instance.data)

        


class MovieRetrieveUpdateDelete(APIView):


    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = Movie.objects.get(id=id)

        serializer_instance = MovieSerializer(qs)

        return Response(data=serializer_instance.data,status=serializer_instance.status)
    


    def put(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        serializer_instance = MovieSerializer(data=request.data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Movie.objects.filter(id=id).update(**cleaned_data)

            return Response(data=serializer_instance.data,status=serializer_instance.status)
        

        else:

            return Response(data=serializer_instance.errors,status=serializer_instance.status)
        


    def delete(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        return Response({"message" : "Deleted"})

        