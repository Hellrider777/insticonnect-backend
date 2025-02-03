from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like_list = models.ManyToManyField(User, related_name='liked_blogs', blank=True)

    def __str__(self):
        return self.title
