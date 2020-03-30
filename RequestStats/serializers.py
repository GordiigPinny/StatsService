import datetime
from rest_framework import serializers
from RequestStats.models import RequestsStats


class RequestsStatsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статистики по запросам
    """
    method = serializers.CharField(max_length=16)
    endpoint = serializers.CharField(max_length=256)
    cb_start_state = serializers.CharField(max_length=16)
    cb_end_state = serializers.CharField(max_length=16)
    queue_length = serializers.IntegerField(min_value=0)
    user_id = serializers.IntegerField(min_value=1, allow_null=True)
    gateway_process_time = serializers.IntegerField(min_value=0)

    class Meta:
        model = RequestsStats
        fields = [
            'id',
            'method',
            'user_id',
            'endpoint',
            'gateway_process_time',
            'status_code',
            'is_fully_processed',
            'cb_start_state',
            'cb_end_state',
            'queue_length',
            'request_dt',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs.get('method', '') not in [x[0] for x in RequestsStats.REQUEST_METHOD_CHOICES]:
            raise serializers.ValidationError('Переданный HTTP метод невалиден')
        if attrs.get('cb_start_state', '') not in [x[0] for x in RequestsStats.CB_STATE_CHOICES]:
            raise serializers.ValidationError('Начальное сосотояние cb невалидено')
        if attrs.get('cb_end_state', '') not in [x[0] for x in RequestsStats.CB_STATE_CHOICES]:
            raise serializers.ValidationError('Начальное сосотояние cb невалидено')
        if isinstance(attrs['request_dt'], str):
            str_dt = attrs['request_dt']
            attrs['request_dt'] = datetime.datetime.strptime(str_dt, '%Y-%m-%dT%H:%M:%SZ')
        return attrs

    def create(self, validated_data):
        new = RequestsStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance
