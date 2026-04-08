from django.core.validators import MinValueValidator
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    author = ...
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
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



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.TextField(verbose_name="Текст ответа")
    order = models.IntegerField(
        verbose_name="Порядок ответа", 
        validators=[MinValueValidator(0)],
        default=0,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.text