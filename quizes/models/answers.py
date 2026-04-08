from django.core.validators import MinValueValidator
from django.db import models

from .questions import Question
from .quiz import QuizAttempt


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answers")
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

    class Meta:
        ordering = ["order", "id"]


class UserAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name="attempt_user_answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_user_answers")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="answer_user_answers", null=True, blank=True)
    custom_answer_text = models.TextField(verbose_name="Текст ответа пользователя", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["attempt", "question"]