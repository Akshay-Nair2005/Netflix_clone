from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.username

class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.FloatField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    cast = models.CharField(max_length=100, default="John Doe, Jane Smith")
    description = models.TextField()
    trailer = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", default="images/default_image.jpg")

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)
    cast = models.CharField(max_length=100, default="John Doe, Jane Smith")
    description = models.TextField()
    trailer = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", default="images/default_image.jpg")

    def __str__(self):
        return self.name

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="seasons")
    number = models.IntegerField()
    episode_count = models.IntegerField()

    def __str__(self):
        return f"Season {self.number} of {self.series.name}"

class Episode(models.Model):
    name = models.CharField(max_length=50)
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="episodes"
    )
    episode_number = models.IntegerField()
    rating = models.FloatField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    trailer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

