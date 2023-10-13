from django.urls import path
from core import views

urlpatterns = [
    path('api/changes/', views.GithubView, name='changes'),
    path('jira/', views.JiraCRUDView, name="jira"),
    path('figma/', views.FigmaView, name="figma"),
    path('figma/comment/', views.FigmaView, name="FILE_COMMENT"),
    path('figma/file_pub/', views.FigmaView, name="file_pub"),
    path('asana/', views.AsanaView, name='asana'),
]
