from django.db import models
from common.models import CommonModel
from users.models import User


# Create your models here.
class Projects(CommonModel):
    user_id = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)


class ProjectFiles(CommonModel):
    project_id = models.ForeignKey(Projects, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='projects/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

