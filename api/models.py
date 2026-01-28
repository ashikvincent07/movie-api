from django.db import models

# Create your models here.
# id,title,year,language,genre,run_time,director

class Movie(models.Model):

    title = models.CharField(max_length=200,unique=True)

    year = models.CharField(max_length=200)

    LANGUAGE_OPTIONS=(
        ("malayalam","malayalam"),
        ("tamil","tamil"),
        ("telungu","telungu"),
        ("kannada","kanada")
    )

    language = models.CharField(max_length=200,choices=LANGUAGE_OPTIONS,default="malayalam")

    GENRE_OPTIONS=(
        ("action","action"),
        ("comedy","comedy"),
        ("drama","drama"),
        ("thriller","thriller"),
        ("fiction","fiction")
    )

    genre = models.CharField(max_length=100,choices=GENRE_OPTIONS,default="action")

    run_time = models.PositiveIntegerField()

    director = models.CharField(max_length=200)

    def __str__(self):
        return self.title




