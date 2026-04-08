from rest_framework import serializers

from quizes.models import Answer, Question


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "text", "order")


class QuestionWithOptionsSerializer(serializers.ModelSerializer):
    answers = AnswerOptionSerializer(many=True, source="question_answers")

    class Meta:
        model = Question
        fields = ("id", "text", "order", "answers")
