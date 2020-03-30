import datetime
from rest_framework import serializers
from AwardsStats.models import PinPurchaseStats, AchievementStats


class PinPurchaseStatSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статы по покупке пинов
    """
    pin_id = serializers.IntegerField(min_value=1)
    user_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = PinPurchaseStats
        fields = [
            'id',
            'pin_id',
            'user_id',
            'purchase_dt',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if isinstance(attrs['purchase_dt'], str):
            str_dt = attrs['purchase_dt']
            attrs['purchase_dt'] = datetime.datetime.strptime(str_dt, '%Y-%m-%dT%H:%M:%SZ')
        return attrs

    def create(self, validated_data):
        new = PinPurchaseStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance


class AchievementStatSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статы по ачивкам
    """
    achievement_id = serializers.IntegerField(min_value=1)
    user_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = AchievementStats
        fields = [
            'id',
            'achievement_id',
            'user_id',
            'achievement_dt',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if isinstance(attrs['achievement_dt'], str):
            str_dt = attrs['achievement_dt']
            attrs['achievement_dt'] = datetime.datetime.strptime(str_dt, '%Y-%m-%dT%H:%M:%SZ')
        return attrs

    def create(self, validated_data):
        new = AchievementStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance
