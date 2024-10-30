from django.db import models

# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок статьи'
    )
    content = models.TextField(
        verbose_name='Содержимое статьи'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
