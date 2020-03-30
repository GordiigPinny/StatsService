from django.db import models


class PinPurchaseStats(models.Model):
    """
    Модель статистики по покупке пинов
    """
    pin_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    purchase_dt = models.DateTimeField()

    def __str__(self):
        return f'User {self.user_id} bought pin {self.pin_id}'


class AchievementStats(models.Model):
    """
    Модель статистики по присуждению достижений
    """
    achievement_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    achievement_dt = models.DateTimeField()

    def __str__(self):
        return f'User {self.user_id} got achievement {self.achievement_id}'
