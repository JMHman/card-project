from django.urls import path
from .views import (
ProjectsDeleteView,
ProjectFilesDeleteView,
ProjectCreateView,
ProjectRetrieveUpdateView,
)


urlpatterns = [
    path('delete/<int:pk>/', ProjectsDeleteView.as_view(), name='projects-delete'),
    path('filesdelete/<int:pk>/', ProjectFilesDeleteView.as_view(), name='projects-files-delete'),
    path('create/', ProjectCreateView.as_view(), name='projects-create'),
    path('detail/<int:id>/', ProjectRetrieveUpdateView.as_view(), name='projects-detail'),
]
