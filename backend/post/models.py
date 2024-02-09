from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.Case)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)


class Like(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Like by {self.user.username} on post {self.post.id}" 