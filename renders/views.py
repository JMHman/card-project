from django.shortcuts import render, redirect
import requests

from django.http import HttpResponse,HttpRequest
from users.forms import UserForm, UrlsForm, NumbersForm
from users.models import Urls, Numbers, User

# Create your views here.

def user_detail_page(request, personal_code):
    # API 엔드포인트 URL 생성
    api_url = f"http://localhost:8000/api/v1/users/detail/{personal_code}/"

    # API에 GET 요청 보내기
    response = requests.get(api_url)

    # 응답 데이터 가져오기
    user_data = response.json()

    # 템플릿에 데이터 전달하여 렌더링
    return render(request, 'home/business_card_user.html', {'user': user_data})

def client_detail_page(request, email):
    # API 엔드포인트 URL 생성
    api_url = f"http://localhost:8000/api/v1/users/client/{email}/"

    # API에 GET 요청 보내기
    response = requests.get(api_url)

    # 응답 데이터 가져오기
    user_data = response.json()

    # 템플릿에 데이터 전달하여 렌더링
    return render(request, 'home/business_card_client.html', {'user': user_data})

def user_login_page(request):
    return render(request, 'users/login.html')

def user_sign_up_page(request):
    return render(request, 'users/sign_up.html')

def user_update_page(request,personal_code):
    api_url = f"http://localhost:8000/api/v1/users/detail/{personal_code}/"
    response = requests.get(api_url)
    user_data = response.json()
    return render(request,'users/user_update.html', {'user': user_data, 'personal_code': personal_code})
