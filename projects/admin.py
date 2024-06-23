from django.contrib import admin
from .models import Projects,ProjectFiles
from users.models import User



class ProjectFilesInline(admin.TabularInline):
    model = ProjectFiles
    extra = 1
    can_delete = True



@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectFilesInline]
    list_display = ('user_id', 'title')
    search_fields = ('user_id', 'title')  # 수정됨
    list_filter = ('user_id', 'title')    # 수정됨
