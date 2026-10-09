from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, verbose_name="Описание")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ['-created_at']  # Знак '-' означает сортировку по убыванию (сначала новые)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title