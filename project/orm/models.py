from django.db import models
from django.utils import timezone
# Create your models here.
# without meta and absract class
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)

# class ISBN(Book):
#     books_ptr = models.OneToOneField(
#         Book, on_delete=models.CASCADE,
#         parent_link=True,
#         primary_key=True,
#     )
#     ISBN = models.TextField()


#Absract Model
class baseItem(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True
        ordering = ['title']

class ItemA(baseItem):
    content = models.TextField()

    class Meta(baseItem.Meta):
        ordering = ['-created']

class ItemB(baseItem):
    file = models.FileField(upload_to='files')

class ItemC(baseItem):
    file = models.FileField(upload_to='image')

class ItemD(baseItem):
    slug = models.SlugField(max_length=255, unique=True)


#Proxy Model
class BookContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class BookOrders(BookContent):
    class Meta:
        proxy = True
        ordering = ['created']

    def created_on(self):
        return timezone.now() -self.created
    
class Books(models.Model):
    title = models.CharField(max_length=100)