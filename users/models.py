from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from common.models import CommonModel
import secrets
import string


# Create your models here.
def generate_random_hex(length):
    return ''.join(secrets.choice(string.hexdigits) for _ in range(length))

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        # Personal code 생성 및 중복 확인 및 재시도
        while True:
            personal_code = generate_random_hex(8)
            if not self.model.objects.filter(personal_code=personal_code).exists():
                user.personal_code = personal_code
                break

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    personal_code = models.CharField(max_length=8, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Mata:
        verbose_name = '사용자'
        verbose_name_plural = "사용자들"

    def save(self, *args, **kwargs):
        # 새로운 사용자일 경우에만 personal_code를 생성하도록 함
        if not self.pk:
            while True:
                personal_code = generate_random_hex(8)
                if not User.objects.filter(personal_code=personal_code).exists():
                    self.personal_code = personal_code
                    break
        super().save(*args, **kwargs)


class Urls(CommonModel):
    user_id = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE)
    url_name = models.CharField(max_length=50,blank=True)
    url = models.URLField(unique=True,blank=True)

    class Meta:
        ordering = ['-url_name']


    def save(self, *args, **kwargs):
        # 입력된 URL을 대문자로 변환하여 저장
        self.url_name = self.url_name.lower()
        super().save(*args, **kwargs)


class Numbers(CommonModel):
    user_id = models.ForeignKey(User, related_name = 'numbers', on_delete=models.CASCADE)
    number_name = models.CharField(max_length=50,blank=True)
    number = models.CharField(max_length=15,blank=True)

    class Meta:
        ordering = ['-number_name']



