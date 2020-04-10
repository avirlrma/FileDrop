from django.urls import path
from dropbox import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view()),
    path('list/<pk>',views.FileView.as_view()),
]