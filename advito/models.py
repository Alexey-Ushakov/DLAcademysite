from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
def user_avatar_path(instance, filename):
    return 'user_{0}/foto/{1}'.format(instance.user.id, filename)

def user_directory_path(instance, filename):
    return 'user_{0}/posts/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='пользователь')
    title = models.CharField(max_length=150, verbose_name='наименование объявления')
    description = models.TextField(max_length=1000, blank=True, verbose_name='содержание объявления')
    image = models.ImageField(upload_to=user_directory_path, verbose_name='фотография товара')
    date_pub = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    date_edit = models.DateTimeField(default=timezone.now, verbose_name='дата изменения')
    price = models.IntegerField(verbose_name='цена товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category',
                                 verbose_name='категория товара')

    def __str__(self):
        return 'Категория: {}  (Пользователь: {}  дата публикации: {}   {}   цена: {})'\
            .format(self.category.title, self.author.username, self.date_pub,
                    self.title, self.price,)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date_pub', 'title']



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='пользователь')
    about = models.TextField(max_length=1000, verbose_name='о себе')
    avatar = models.ImageField(upload_to=user_avatar_path, verbose_name='фото пользователя')
    birth_date = models.DateField(null=True, blank=True, verbose_name='день рождения')
    created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=True, blank=True, related_name='post',
        verbose_name='объявления')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профели'