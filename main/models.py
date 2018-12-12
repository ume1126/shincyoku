from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# https://qiita.com/okoppe8/items/a1149b2be54441951de1#%E6%95%B4%E6%95%B0integerfield
PLACE_CHOICE = (
    ('ohuton', 'おふとん'),
    ('ouchi', 'おうち'),
    ('cafe','カフェ'),)
THEME_CHOICE = (
    ('illust', 'イラスト'),
    ('photo', '写真'),
    ('text', '小説'),
    ('program', 'プログラミング'),
    ('other', 'その他'),
    ('multi', 'マルチ'),)

# ―――――――――――――――――――
class Room(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #ユーザー
    title = models.CharField(max_length=140)
    place = models.CharField(max_length=20, choices=PLACE_CHOICE)
    theme = models.CharField(max_length=20, choices=THEME_CHOICE)
    start_date = models.DateField(
        blank=True,
        null=True,
        default=timezone.now,)
    start_time = models.TimeField(
        blank=True,
        null=True,
        default=timezone.now,)
    end_date = models.DateField(
        blank=True,
        null=True,
        default=timezone.now,)
    end_time = models.TimeField(
        blank=True,
        null=True,
        default=timezone.now()+timezone.timedelta(hours=1))
        # https://sleepless-se.net/2018/06/09/django%E3%83%A2%E3%83%87%E3%83%ABmodels-datetimefield%E3%81%AB%E7%8F%BE%E5%9C%A8%E3%81%AE%E6%99%82%E9%96%93%E3%82%92%E6%8C%BF%E5%85%A5%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/
    class Meta:
        ordering = ['-start_date']


# ―――――――――――――――――――
class Shincyoku(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #ユーザー
    snck = models.CharField(max_length=140)
    fight = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)

    progress = models.IntegerField(
                              default=0,
                              validators=[MinValueValidator(0),
                                          MaxValueValidator(100)])

    # def summary(self):
    #     return self.text[:15]
    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.snck


# ―――――――――――――――――――
