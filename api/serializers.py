from rest_framework import serializers

from api.models import Movie



class MovieSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    title = serializers.CharField()

    year = serializers.CharField()

    language = serializers.CharField()

    genre = serializers.ChoiceField(Movie.GENRE_OPTIONS)

    run_time = serializers.IntegerField()

    director = serializers.CharField()



    def validate(self, data):
        
        if data.get("run_time") < 60 or data.get("run_time") > 360:


            raise serializers.ValidationError("runtime should be > 60 and < 360")
        

        title = data.get("title")

        qs = Movie.objects.filter(title=title)

        if qs.exists():

            raise serializers.ValidationError("movie already exists")
        
        return data
    



class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField()

    password = serializers.CharField()

    email = serializers.EmailField()

    first_name = serializers.CharField()

    last_name = serializers.CharField()
