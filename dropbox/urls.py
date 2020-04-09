from django.urls import path
from dropbox import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view()),
    #path('dropbox/list',views.list_files)
]