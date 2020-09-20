from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre

class GameNews(models.Model):
    title = models.CharField(max_length=60)
    year_of_issue =models.DateField()
    developer= models.CharField(max_length=60)
    publisher= models.CharField(max_length=60)
    version= models.CharField(max_length=60)
    repack_author= models.CharField(max_length=60)
    interface_language= models.CharField(max_length=60)
    voice_Language= models.CharField(max_length=60)
    subtitles = models.CharField(max_length=60)
    Tablet= models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    repack = models.TextField(max_length=1000)
    min_os = models.CharField(max_length=30)
    min_processor= models.CharField(max_length=30)
    min_memory= models.CharField(max_length=30)
    min_graphics= models.CharField(max_length=30)
    min_storage= models.CharField(max_length=30)
    min_sound_card= models.CharField(max_length=30)
    os= models.CharField(max_length=30)
    processor= models.CharField(max_length=30)
    memory= models.CharField(max_length=30)
    graphics= models.CharField(max_length=30)
    storage= models.CharField(max_length=30)
    sound_card= models.CharField(max_length=30)
    Hot_News = models.BooleanField(default=False)
    main_image= models.ImageField()
    news_image1= models.ImageField()
    news_image2= models.ImageField()
    news_image3= models.ImageField()
    news_image4= models.ImageField()
    video_trailer= models.CharField(max_length=50)
    video_gameplay= models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre)
    data = models.FileField(upload_to='torrent-files')
    def __str__(self):
        return self.title

class UpComingGames(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    main_image= models.ImageField()
    main_image2= models.ImageField()
    news_image1= models.ImageField()
    news_image2= models.ImageField()
    news_image3= models.ImageField()
    news_image4= models.ImageField()
    video_trailer= models.CharField(max_length=50)





