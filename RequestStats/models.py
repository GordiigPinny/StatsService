from django.db import models


class RequestsStats(models.Model):
    """
    Модель для сбора статистики по запросам
    """
    REQUEST_METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
    )
    CB_STATE_CHOICES = (
        ('OPEN', 'OPEN'),
        ('HALF-OPEN', 'HALF-OPEN'),
        ('CLOSED', 'CLOSED'),
    )

    method = models.CharField(max_length=16, choices=REQUEST_METHOD_CHOICES)
    user_id = models.PositiveIntegerField(null=True, default=None)  # None == незарегестрированный
    endpoint = models.CharField(max_length=256)
    gateway_process_time = models.FloatField()
    status_code = models.PositiveIntegerField()
    is_fully_processed = models.BooleanField(default=True)
    cb_start_state = models.CharField(max_length=16, choices=CB_STATE_CHOICES, default='CLOSE')
    cb_end_state = models.CharField(max_length=16, choices=CB_STATE_CHOICES, default='CLOSE')
    queue_length = models.PositiveIntegerField()
    request_dt = models.DateTimeField()

    def __str__(self):
        return f'{self.method} {self.endpoint} by {self.user_id if self.user_id else "anon"}'
