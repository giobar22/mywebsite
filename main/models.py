from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class GameNews(models.Model):
    title = models.CharField(max_length=60)
    year_of_issue = models.DateField()
    developer = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    version = models.CharField(max_length=60)
    repack_author = models.CharField(max_length=60)
    interface_language = models.CharField(max_length=60)
    voice_Language = models.CharField(max_length=60)
    subtitles = models.CharField(max_length=60)
    tablet = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    repack = models.TextField(max_length=1000)
    min_os = models.CharField(max_length=60)
    min_processor = models.CharField(max_length=60)
    min_memory = models.CharField(max_length=60)
    min_graphics = models.CharField(max_length=60)
    min_storage = models.CharField(max_length=60)
    min_sound_card = models.CharField(max_length=60)
    os = models.CharField(max_length=60)
    processor = models.CharField(max_length=60)
    memory = models.CharField(max_length=60)
    graphics = models.CharField(max_length=60)
    storage = models.CharField(max_length=60)
    sound_card = models.CharField(max_length=60)
    Hot_News = models.BooleanField(default=False)
    main_image = models.ImageField()
    news_image1 = models.ImageField()
    news_image2 = models.ImageField()
    news_image3 = models.ImageField()
    news_image4 = models.ImageField()
    video_trailer = models.CharField(max_length=50)
    video_gameplay = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre)
    data = models.FileField(upload_to='torrent-files')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    games_view = models.IntegerField(default=0, null=True, blank=True)
    download = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_download(self):
        return self.download.count()

    def get_absolute_url(self):
        return reverse('game_details', args=[str(self.id)])


class UpComingGames(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    main_image = models.ImageField()
    main_image2 = models.ImageField()
    news_image1 = models.ImageField()
    news_image2 = models.ImageField()
    news_image3 = models.ImageField()
    news_image4 = models.ImageField()
    video_trailer = models.CharField(max_length=50)


class Logo(models.Model):
    logo_image = models.ImageField(upload_to='logo_image')
