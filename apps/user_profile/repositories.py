from apps.user_profile.models import Profile, WeightHistory, BodyFatPercentageHistory, MuscleMassHistory
from typing import List, Optional, Any

class ProfileRepository:
    def __init__(
        self,
        model: type[Profile] = Profile
    ) -> None:
        self.model = model

    def create(
        self,
        data: dict[str, Any]
    ) -> Profile:
        """
        渡したデータを使って新しいモデルインスタンスを作成する関数
        """
        try:
            instance = self.model.objects.create(**data)
            return instance
        except Exception as e:
            raise ValueError(f"Failed to create profile: {e}")

    def get_by_id(
        self,
        obj_id: int
    ) -> Optional[Profile]:
        """
        指定したIDのデータを取得する関数
        """
        try:
            return self.model.objects.filter(id=obj_id).first()
        except Profile.DoesNotExist:
            return None

    def list(self) -> List[Profile]:
        """
        データの一覧を取得する関数
        """
        return list(self.model.objects.all().order_by("created_at"))

    def update(
        self,
        instance: Profile,
        data: dict[str, Any]
    ) -> Profile:
        """
        渡したモデルを更新する関数
        """
        # 性別
        instance.gender = data["gender"]
        # ニックネーム
        instance.nickName = data["nickName"]
        # 身長
        instance.height = data["height"]
        # 生年月日
        instance.dateOfBirth = data["dateOfBirth"]

        instance.save()
        return instance

    def delete(self, instance: Profile) -> int:
        """
        渡したモデルオブジェクトを削除する関数
        """
        deleted_count, _ =instance.delete()
        return deleted_count


class WeightHistoryRepository:
    def __init__(
        self,
        model: type[WeightHistory] = WeightHistory
    ) -> None:
        self.model = model

    def create(
        self,
        data: dict[str, Any]
    ) -> WeightHistory:
        """
        渡したデータを使って新しいモデルインスタンスを作成する関数
        """
        try:
            instance = self.model.objects.create(**data)
            return instance
        except Exception as e:
            raise ValueError(f"Failed to create WeightHistory: {e}")

    def get_by_id(
        self,
        obj_id: int
    ) -> Optional[WeightHistory]:
        """
        指定したIDのデータを取得する関数
        """
        try:
            return self.model.objects.filter(id=obj_id).first()
        except WeightHistory.DoesNotExist:
            return None

    def list(self) -> List[WeightHistory]:
        """
        データの一覧を取得する関数
        """
        return list(self.model.objects.all().order_by("created_at"))

    def update(
        self,
        instance: WeightHistory,
        data: dict[str, Any]
    ) -> WeightHistory:
        """
        渡したモデルを更新する関数
        """
        # 日付
        instance.date = data["date"]
        # 体重
        instance.weight = data["weight"]

        instance.save()
        return instance

    def delete(self, instance: WeightHistory) -> int:
        """
        渡したモデルオブジェクトを削除する関数
        """
        deleted_count, _ =instance.delete()
        return deleted_count


class BodyFatPercentageHistoryRepository:
    def __init__(
        self,
        model: type[BodyFatPercentageHistory] = BodyFatPercentageHistory
    ) -> None:
        self.model = model

    def create(
        self,
        data: dict[str, Any]
    ) -> BodyFatPercentageHistory:
        """
        渡したデータを使って新しいモデルインスタンスを作成する関数
        """
        try:
            instance = self.model.objects.create(**data)
            return instance
        except Exception as e:
            raise ValueError(f"Failed to create BodyFatPercentageHistory: {e}")

    def get_by_id(
        self,
        obj_id: int
    ) -> Optional[BodyFatPercentageHistory]:
        """
        指定したIDのデータを取得する関数
        """
        try:
            return self.model.objects.filter(id=obj_id).first()
        except BodyFatPercentageHistory.DoesNotExist:
            return None

    def list(self) -> List[BodyFatPercentageHistory]:
        """
        データの一覧を取得する関数
        """
        return list(self.model.objects.all().order_by("created_at"))

    def update(
        self,
        instance: BodyFatPercentageHistory,
        data: dict[str, Any]
    ) -> BodyFatPercentageHistory:
        """
        渡したモデルを更新する関数
        """
        # 日付
        instance.date = data["date"]
        # 体脂肪率
        instance.bodyFatPercentage = data["bodyFatPercentage"]

        instance.save()
        return instance

    def delete(self, instance: BodyFatPercentageHistory) -> int:
        """
        渡したモデルオブジェクトを削除する関数
        """
        deleted_count, _ =instance.delete()
        return deleted_count


class MuscleMassHistoryRepository:
    def __init__(
        self,
        model: type[MuscleMassHistory] = MuscleMassHistory
    ) -> None:
        self.model = model

    def create(
        self,
        data: dict[str, Any]
    ) -> MuscleMassHistory:
        """
        渡したデータを使って新しいモデルインスタンスを作成する関数
        """
        try:
            instance = self.model.objects.create(**data)
            return instance
        except Exception as e:
            raise ValueError(f"Failed to create MuscleMassHistory: {e}")

    def get_by_id(
        self,
        obj_id: int
    ) -> Optional[MuscleMassHistory]:
        """
        指定したIDのデータを取得する関数
        """
        try:
            return self.model.objects.filter(id=obj_id).first()
        except MuscleMassHistory.DoesNotExist:
            return None

    def list(self) -> List[MuscleMassHistory]:
        """
        データの一覧を取得する関数
        """
        return list(self.model.objects.all().order_by("created_at"))

    def update(
        self,
        instance: MuscleMassHistory,
        data: dict[str, Any]
    ) -> MuscleMassHistory:
        """
        渡したモデルを更新する関数
        """
        # 日付
        instance.date = data["date"]
        # 筋肉量
        instance.muscleMass = data["muscleMass"]

        instance.save()
        return instance

    def delete(self, instance: MuscleMassHistory) -> int:
        """
        渡したモデルオブジェクトを削除する関数
        """
        deleted_count, _ =instance.delete()
        return deleted_count