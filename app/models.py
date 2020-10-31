from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GameRomm(models.Model):
    game_title = models.CharField(db_column='제목', max_length=200, null=False, blank=False)
    game_status = models.BooleanField(db_column='진행 여부', default='Y', null=False, blank=False)
    game_date = models.DateTimeField(db_column='생성 시간', default=timezone.now, null=False, blank=False)

    def __str__(self):
        return self.game_title

class ChoiceNum(models.Model):
    choice = models.ForeignKey(GameRomm, on_delete=models.CASCADE, null=True, related_name='choice')
    choice_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    choice_num = models.IntegerField(default=0, null=False, blank=False)
    
    class Meta:
        ordering = ['-id']
            
    def __str__(self):
        return '%s - %s' % (self.choice_user, self.choice_num) 


class BeatNum(models.Model):
    beat = models.ForeignKey(ChoiceNum, on_delete=models.CASCADE, null=True, related_name='beat')
    beat_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    beat_num = models.IntegerField(default=0, null=False, blank=False)
    beat_result = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        ordering = ['-id']
            
    def __str__(self):
        return '%s - %s' % (self.beat_user, self.beat_num) 
