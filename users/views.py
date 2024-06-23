
from rest_framework import generics
from .models import Urls, Numbers, User
from .serializers import UserSerializer,NumbersSerializer,UrlsSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse



from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            user_data = {
                'id': user.id,
                'email': user.email,
                'personal_code': user.personal_code,
                # 필요한 다른 필드 추가 가능
            }
            return JsonResponse({
                'token': token.key,
                'user': user_data,
                'personal_code': user.personal_code
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all().prefetch_related('numbers', 'urls')
    serializer_class = UserSerializer
    lookup_field = 'personal_code'

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

class ClientRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all().prefetch_related('numbers', 'urls')
    serializer_class = UserSerializer
    lookup_field = 'email'

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all().prefetch_related('numbers', 'urls', 'projects')
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'personal_code'


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'personal_code'


class UrlsDeleteView(generics.DestroyAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer


class NumbersDeleteView(generics.DestroyAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer


