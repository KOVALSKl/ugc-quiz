from django.urls import path

from quizes.views import QuizCurrentQuestionView

urlpatterns = [
    path(
        "quizzes/<int:pk>/current-question/",
        QuizCurrentQuestionView.as_view(),
        name="quiz-current-question",
    ),
]
