from rest_framework import serializers
from .models import Projects, ProjectFiles


class ProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFiles
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ProjectsSerializer(serializers.ModelSerializer):
    files = ProjectFilesSerializer(many=True,required=False)

    class Meta:
        model = Projects
        fields = '__all__'