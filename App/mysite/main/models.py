from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    categories = models.ManyToManyField(Category, related_name="posts")
    image = models.ImageField(null=True ,blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    parent_comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="child_comments", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="comments")
    text = models.TextField()

    def __str__(self):
        return f'{self.author.name} - {self.text}'