from django.core.validators import MinValueValidator
from django.db import models

from .quiz import Quiz


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz_questions")
    text = models.TextField(verbose_name="Текст вопроса")
    order = models.IntegerField(
        verbose_name="Порядок вопроса", 
        validators=[MinValueValidator(0)],
        default=0,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["order", "id"]
        
