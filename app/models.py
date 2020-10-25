from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GameRomm(models.Model):
    game_title = models.CharField(db_column='제목', max_length=200, null=False, blank=False)
    game_status = models.BooleanField(db_column='진행 여부', default='Y', null=False, blank=False)
    game_date = models.DateTimeField(db_column='생성 시간', default=timezone.now, null=False, blank=False)

    def __str__(self):
        return self.game_title

class GameNum(models.Model):
    game = models.ForeignKey(GameRomm, on_delete=models.CASCADE, null=True, related_name='game')
    game_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    game_num = models.IntegerField(default=0, null=False, blank=False)
    
    class Meta:
        ordering = ['-id']
            
    def __str__(self):
        return '%s - %s' % (self.game_user, self.game_num) 
