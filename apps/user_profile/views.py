from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user_profile.serializers import ProfileSerializer, WeightHistorySerializer, BodyFatPercentageHistorySerializer, MuscleMassHistorySerializer
from apps.user_profile.repositories import ProfileRepository, WeightHistoryRepository, BodyFatPercentageHistoryRepository, MuscleMassHistoryRepository


class ProfileCreateView(APIView):
    def post(self, request):
        """
        プロフィール新規作成
        """
        try:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                repo = ProfileRepository()
                profile = repo.create(data=serializer.validated_data)
                serialized_profile = ProfileSerializer(profile)
                return Response(serialized_profile.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProfileView(APIView):
    def get(self, request, **kwargs):
        """
        プロフィール取得
        """
        try:
            profile_id = kwargs.get('profileId')
            repo = ProfileRepository()
            profile = repo.get_by_id(obj_id=profile_id)
            serialized_profile = ProfileSerializer(profile)
            return Response(serialized_profile.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, **kwargs):
        """
        プロフィール更新
        """
        try:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                # URIからユーザーIDを取得
                profile_id = kwargs.get('profileId')

                repo = ProfileRepository()
                profile = repo.get_by_id(obj_id=profile_id)

                updated_profile = repo.update(instance=profile, data=serializer.validated_data)
                serialized_profile = ProfileSerializer(updated_profile)
                return Response(serialized_profile.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, **kwargs):
        """
        プロフィール削除
        """
        try:
            # URIからユーザーIDを取得
            profile_id = kwargs.get('profileId')

            repo = ProfileRepository()
            profile = repo.get_by_id(obj_id=profile_id)
            if not profile:
                return Response({"error": f"no such data profile_id: {profile_id}"}, status=status.HTTP_404_NOT_FOUND)
            _ = repo.delete(instance=profile)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeightHistoryView(APIView):
    def post(self, request, **kwargs):
        """
        体重データ新規作成
        """
        try:
            serializer = WeightHistorySerializer(data=request.data)
            if serializer.is_valid():
                profile_id = kwargs.get("profileId")
                profile_repo = ProfileRepository()
                weight_history_repo = WeightHistoryRepository()
                profile = profile_repo.get_by_id(obj_id=profile_id)

                weight_history_data = {
                    "profile": profile,
                    "weight": serializer.validated_data["weight"],
                    "date": serializer.validated_data["date"]
                }
                weight_history = weight_history_repo.create(data=weight_history_data)

                serialized_weight_history = WeightHistorySerializer(weight_history)
                return Response(serialized_weight_history.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BodyFatPercentageHistoryView(APIView):
    def post(self, request, **kwargs):
        """
        体脂肪率データ新規作成
        """
        try:
            serializer = BodyFatPercentageHistorySerializer(data=request.data)
            if serializer.is_valid():
                profile_id = kwargs.get("profileId")
                profile_repo = ProfileRepository()
                bf_percentage_history_repo = BodyFatPercentageHistoryRepository()
                profile = profile_repo.get_by_id(obj_id=profile_id)

                bf_percentage_history_data = {
                    "profile": profile,
                    "bodyFatPercentage": serializer.validated_data["bodyFatPercentage"],
                    "date": serializer.validated_data["date"]
                }
                bf_percentage_history = bf_percentage_history_repo.create(data=bf_percentage_history_data)

                serialized_bf_percentage_history = BodyFatPercentageHistorySerializer(bf_percentage_history)
                return Response(serialized_bf_percentage_history.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MuscleMassHistoryView(APIView):
    def post(self, request, **kwargs):
        """
        筋肉量データ新規作成
        """
        try:
            serializer = MuscleMassHistorySerializer(data=request.data)
            if serializer.is_valid():
                profile_id = kwargs.get("profileId")
                profile_repo = ProfileRepository()
                muscle_mass_history_repo = MuscleMassHistoryRepository()
                profile = profile_repo.get_by_id(obj_id=profile_id)

                muscle_mass_history_data = {
                    "profile": profile,
                    "muscleMass": serializer.validated_data["muscleMass"],
                    "date": serializer.validated_data["date"]
                }
                muscle_mass_percentage_history = muscle_mass_history_repo.create(data=muscle_mass_history_data)

                serialized_muscle_mass_percentage_history = MuscleMassHistorySerializer(muscle_mass_percentage_history)
                return Response(serialized_muscle_mass_percentage_history.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)