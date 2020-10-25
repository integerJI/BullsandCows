from django.db import models
from django.utils import timezone


class GameRomm(models.Model):
    game_title = models.CharField(db_column='제목', max_length=200, null=False, blank=False)
    game_status = models.BooleanField(db_column='진행 여부', default='Y', null=False, blank=False)
    game_date = models.DateTimeField(db_column='생성 시간', default=timezone.now, null=False, blank=False)

    def __str__(self):
        return self.game_title
