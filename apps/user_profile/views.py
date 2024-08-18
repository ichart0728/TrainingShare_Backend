from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from firebase_admin import auth
from rest_framework.permissions import IsAuthenticated
from apps.user_profile.serializers import ProfileSerializer
from apps.user_profile.repositories import ProfileRepository


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