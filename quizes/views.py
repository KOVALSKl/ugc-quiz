from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from quizes.models import Quiz, QuizAttempt, UserAnswer
from quizes.serializers import QuestionWithOptionsSerializer


class QuizCurrentQuestionView(APIView):
    """
    Следующий по порядку (order, id) вопрос без ответа в текущей попытке пользователя.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)

        attempt = (
            QuizAttempt.objects.filter(
                quiz=quiz, user=request.user, is_completed=False
            )
            .order_by("-started_at")
            .first()
        )
        if attempt is None:
            attempt = QuizAttempt.objects.create(quiz=quiz, user=request.user)

        answered_ids = set(
            UserAnswer.objects.filter(attempt=attempt).values_list(
                "question_id", flat=True
            )
        )

        questions = (
            quiz.quiz_questions.order_by("order", "id")
            .prefetch_related("question_answers")
        )
        for question in questions:
            if question.id not in answered_ids:
                serializer = QuestionWithOptionsSerializer(question)
                return Response(
                    {
                        "completed": False,
                        "attempt_id": attempt.pk,
                        "question": serializer.data,
                    }
                )

        return Response(
            {
                "completed": True,
                "attempt_id": attempt.pk,
                "question": None,
            }
        )
