from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body =models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True) ### change to date posted
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    @property
    def number_of_comments(self):
        return Comment.objects.filter(comment_post=self).count()




class Comment(models.Model):
    comment_post = models.ForeignKey(
        Post,
         on_delete=models.CASCADE,
         related_name = 'comments',
         )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)


    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('home') # make a change here later



    