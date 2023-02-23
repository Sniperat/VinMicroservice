from rest_framework import serializers
from .models import DetailModel, WeightModel


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightModel
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    weight = WeightSerializer(many=True)

    class Meta:
        model = DetailModel
        fields = '__all__'
