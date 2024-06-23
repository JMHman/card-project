from rest_framework import serializers
from users.models import User,Urls,Numbers
from projects.models import Projects,ProjectFiles
from projects.serializers import ProjectsSerializer


class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    numbers = NumbersSerializer(many=True, required=False)
    urls = UrlsSerializer(many=True, required=False)
    projects = ProjectsSerializer(many=True, required=False)
    confirm_password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ("id", "name", "email", "numbers", "urls", "projects", "password", "confirm_password", "personal_code")
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'id': {'read_only': True},
            'personal_code':{'read_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")
        return data

    def create(self, validated_data):
        numbers_data = validated_data.pop('numbers', [])
        urls_data = validated_data.pop('urls', [])
        projects_data = validated_data.pop('projects', [])
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        for number_data in numbers_data:
            Numbers.objects.create(user=user, **number_data)

        for url_data in urls_data:
            Urls.objects.create(user=user, **url_data)

        for project_data in projects_data:
            files_data = project_data.pop('files', [])
            project = Projects.objects.create(user=user, **project_data)
            for file_data in files_data:
                ProjectFiles.objects.create(project=project, **file_data)

        return user

    def update(self, instance, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        if confirm_password is not None and confirm_password != validated_data.get('password'):
            raise serializers.ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")

        # numbers_data = validated_data.pop('numbers', [])
        # urls_data = validated_data.pop('urls', [])
        # projects_data = validated_data.pop('projects', [])

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        for number_data in numbers_data:
            Numbers.objects.create(user=instance, **number_data)

        for url_data in urls_data:
            Urls.objects.create(user=instance, **url_data)

        for project_data in projects_data:
            files_data = project_data.pop('files', [])
            project, created = Projects.objects.update_or_create(user=instance, **project_data)

            for file_data in files_data:
                ProjectFiles.objects.create(project=project, **file_data)

        return instance
