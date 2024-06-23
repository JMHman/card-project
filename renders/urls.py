from django.urls import path
from .views import *

urlpatterns = [
    # path('detail/<str:personal_code>/front/', user_detail_view, name='user-detail-front'),
    # path('detail/<str:personal_code>/back/', user_detail_back_view, name='user-detail-back'),
    path('detail/<str:personal_code>/', user_detail_page, name='user-detail'),
    path('client/<str:email>/', client_detail_page, name='client-detail'),
    path('login/', user_login_page, name='user-login'),
    path('sign-up/', user_sign_up_page, name='user-sign-up'),
    path('update/<str:personal_code>/', user_update_page, name='user-update'),
]