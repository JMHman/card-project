from django.contrib import admin

from .models import User, Urls, Numbers

# Register your models here.
class UrlsInline(admin.TabularInline):
    model = Urls
    extra = 1
    can_delete = True
    verbose_name_plural = '주소들 / Urls'
    verbose_name = '주소 / url'


class NumbersInline(admin.TabularInline):
    model = Numbers
    extra = 1
    can_delete = True
    verbose_name_plural = '전화번화들 / Numbers'
    verbose_name = '전화번호 / Number'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name','personal_code')
    search_fields = ('email', 'name')
    list_filter = ('is_staff', 'is_active')
    inlines = [UrlsInline, NumbersInline]