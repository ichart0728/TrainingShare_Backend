from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from firebase_admin import auth
from apps.user.models import User
from django.utils.timezone import now
from apps.user.serializers import UserSerializer
from apps.user.repositories import UserRepository

class FirebaseCreateUserView(APIView):
    """
    Firebase Authenticationを使用して新規ユーザーを作成するビュー
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():
                # リクエストから必要なデータを取得
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                # Firebaseで新しいユーザーを作成
                firebase_user = auth.create_user(
                    email=email,
                    password=password
                )

                uid = firebase_user.uid

                # Djangoで新しいユーザーを作成
                user_repo = UserRepository()
                data = {
                    'uid': uid,
                    'email': email,
                    'date_joined': now(),
                    'is_active': True,
                }
                user_data = user_repo.create(data=data)
                serialized_user = UserSerializer(user_data)

                return Response({"message": serialized_user.data}, status=status.HTTP_201_CREATED)


            else:
                return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        except auth.EmailAlreadyExistsError:
            return Response({"error": "Email already exists in Firebase"}, status=status.HTTP_400_BAD_REQUEST)
        except auth.InvalidPasswordError:
            return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
        except auth.FirebaseError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)