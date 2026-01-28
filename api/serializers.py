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

        self.status = 200
        
        if data.get("run_time") < 60 or data.get("run_time") > 360:

            self.status = 422

            raise serializers.ValidationError("runtime should be > 60 and < 360")
        

        title = data.get("title")

        qs = Movie.objects.filter(title=title)

        if qs.exists():

            self.status = 409

            raise serializers.ValidationError("movie already exists")
        
        return data
