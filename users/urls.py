from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import (
    UserRetrieveView,
    UserListView,
    UserUpdateView,
    UserDeleteView,
    UrlsDeleteView,
    NumbersDeleteView,
    LoginView,
    UserCreateView,
    ClientRetrieveView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', UserCreateView.as_view(), name="sign-up"),
    path('list/', UserListView.as_view(), name='users-list'),
    path('detail/<str:personal_code>/', UserRetrieveView.as_view(), name='user-detail'),
    path('update/<str:personal_code>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<str:personal_code>/', UserDeleteView.as_view(), name='user-delete'),
    path('urls/<int:pk>/', UrlsDeleteView.as_view(), name='urls-delete'),
    path('numbers/<int:pk>/', NumbersDeleteView.as_view(), name='numbers-delete'),
    path('client/<str:email>/',ClientRetrieveView.as_view(), name='client-retrieve'),
]
