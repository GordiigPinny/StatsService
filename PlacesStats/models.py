from django.db import models


class PlaceStats(models.Model):
    """
    Модель статистики по изменению мест
    """
    ACTION_CHOICES = (
        ('OPENED', 'OPENED'),
        ('CREATED', 'CREATED'),
        ('EDITED', 'EDITED'),
        ('DELETED', 'DELETED'),
    )

    action = models.CharField(max_length=16, choices=ACTION_CHOICES)
    place_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField(null=True)
    action_dt = models.DateTimeField()

    def __str__(self):
        return f'{self.action} {self.place_id} by  {self.user_id if self.user_id else "anon"}'


class AcceptStats(models.Model):
    """
    Модель статистики по подтверждениям мест
    """
    ACTION_CHOICES = (
        ('ACCEPTED', 'ACCEPTED'),
        ('DECLINED', 'DECLINED'),
    )

    action = models.CharField(max_length=16, choices=ACTION_CHOICES)
    place_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    action_dt = models.DateTimeField()

    def __str__(self):
        return f'{self.action} {self.place_id} by {self.user_id}'


class RatingStats(models.Model):
    """
    Модель статистики по рейтингу
    """
    place_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    old_rating = models.PositiveIntegerField()
    new_rating = models.PositiveIntegerField()
    action_dt = models.DateTimeField()

    def __str__(self):
        return f'{self.old_rating} -> {self.new_rating} on {self.place_id} by {self.user_id}'
