from django.db import models

# Create your models here.
    
class Author(models.Model):
    # b_title=models.CharField(max_length=100,blank=False,default="blog")
    auth_name=models.CharField("Author Name ", max_length=50, default='author')

    def __str__(self) -> str:
        return self.auth_name
    
class Blog(models.Model):
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE)
    b_title=models.CharField(
        "Blog Name ",
        max_length=100, 
        blank=False, 
        default="blog")

    def __str__(self) -> str:
        return self.b_title