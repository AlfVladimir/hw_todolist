from django.db import models
from datetime import datetime

# Create your models here.


class Tasklist(models.Model):
    """Список задач"""

    text = models.CharField(max_length=100, help_text="Задача")
    is_done = models.BooleanField(default=False, help_text="Выполнена")
    timestamp_create = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, help_text="Когда создана"
    )
    timestamp_done = models.DateTimeField(
        null=True, blank=True, help_text="Когда выполнена"
    )

    def save(self, *args, **kwargs) -> None:
        """
        Ставим время окончания, если задача сделана
        """
        if self.is_done and self.timestamp_done is None:
            self.timestamp_done = datetime.now()

        if not self.is_done and self.timestamp_done:
            self.timestamp_done = None

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Задача {self.text[:30]}..."
