# models.py
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """
    共通の親モデル
    「作成日時」「更新日時」を持つ
    すべてのモデルはこのモデルを継承する
    """
    created_at = models.DateTimeField("作成日時", default=timezone.now)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        abstract = True