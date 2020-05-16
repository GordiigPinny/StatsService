import datetime
from rest_framework import serializers
from RequestStats.models import RequestsStats


class RequestsStatsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статистики по запросам
    """
    method = serializers.ChoiceField(choices=RequestsStats.REQUEST_METHOD_CHOICES)
    endpoint = serializers.CharField(max_length=256, allow_blank=False, allow_null=False)
    user_id = serializers.IntegerField(min_value=1, allow_null=True)
    process_time = serializers.FloatField(min_value=0)

    class Meta:
        model = RequestsStats
        fields = [
            'id',
            'method',
            'user_id',
            'endpoint',
            'status_code',
            'process_time',
            'request_dt',
        ]

    def create(self, validated_data):
        new = RequestsStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance
