from apps.user.models import User
from typing import List, Optional, Any

class UserRepository:
    def __init__(
        self,
        model: type[User] = User
    ) -> None:
        self.model = model

    def create(
        self,
        data: dict[str, Any]
    ) -> User:
        """
        渡したデータを使って新しいモデルインスタンスを作成する関数
        """
        try:
            instance = self.model.objects.create(**data)
            return instance
        except Exception as e:
            raise ValueError(f"Failed to create User: {e}")

    def get_by_id(
        self,
        obj_id: int
    ) -> Optional[User]:
        """
        指定したIDのデータを取得する関数
        """
        try:
            return self.model.objects.filter(id=obj_id).first()
        except User.DoesNotExist:
            return None

    def delete(self, instance: User) -> int:
        """
        渡したモデルオブジェクトを削除する関数
        """
        deleted_count, _ =instance.delete()
        return deleted_count