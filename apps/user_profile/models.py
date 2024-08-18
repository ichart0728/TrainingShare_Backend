from django.db import models
from django.conf import settings
from apps.model_utils.models import BaseModel

# プロフィールテーブル (Profile) のモデル
class Profile(BaseModel):
    # ニックネーム
    nickName = models.CharField(max_length=20)
    # ユーザーとプロフィールを1:1で紐づける
    # ユーザーが削除されたらプロフィールも削除されるように設定
    userProfile = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='userProfile',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    # 性別
    GENDER_CHOICES = (
        ('男性', '男性'),
        ('女性', '女性'),
        ('その他', 'その他'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    # 身長
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # 生年月日
    dateOfBirth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nickName


# 以下3つは物理的には別モデルだが、論理的にはプロフィールの一部なので当該ファイルで定義する
# 体重履歴テーブル (WeightHistory) のモデル
class WeightHistory(models.Model):
    # プロフィールと体重履歴を1:Nで紐づける
    profile = models.ForeignKey(Profile, related_name='weightHistory', on_delete=models.CASCADE)
    # 体重
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    # 記録日
    date = models.DateField()

    def __str__(self):
        return f"{self.profile.nickName} - {self.date}"


# 体脂肪率履歴テーブル (BodyFatPercentageHistory) のモデル
class BodyFatPercentageHistory(models.Model):
    # プロフィールと体脂肪率履歴を1:Nで紐づける
    profile = models.ForeignKey(Profile, related_name='bodyFatPercentageHistory', on_delete=models.CASCADE)
    # 体脂肪率
    bodyFatPercentage = models.DecimalField(max_digits=5, decimal_places=2)
    # 記録日
    date = models.DateField()

    def __str__(self):
        return f"{self.profile.nickName} - {self.date}"


# 筋肉量履歴テーブル (MuscleMassHistory) のモデル
class MuscleMassHistory(models.Model):
    # プロフィールと筋肉量履歴を1:Nで紐づける
    profile = models.ForeignKey(Profile, related_name='muscleMassHistory', on_delete=models.CASCADE)
    # 筋肉量
    muscleMass = models.DecimalField(max_digits=5, decimal_places=2)
    # 記録日
    date = models.DateField()

    def __str__(self):
        return f"{self.profile.nickName} - {self.date}"