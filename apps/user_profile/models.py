from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
import uuid
from apps.model_utils.models import BaseModel

# プロフィールテーブル (Profile) のモデル
class Profile(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
