from rest_framework import generics

from .serializers import ProjectsSerializer,ProjectFilesSerializer
from .models import Projects,ProjectFiles

class ProjectsDeleteView(generics.DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectFilesDeleteView(generics.DestroyAPIView):
    queryset = ProjectFiles.objects.all()
    serializer_class = ProjectFilesSerializer


class ProjectCreateView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Projects.objects.all().prefetch_related("files").order_by('-updated_at')
    serializer_class = ProjectsSerializer



