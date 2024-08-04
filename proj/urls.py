from django.contrib import admin
from django.urls import path
from app.views import BlogDetail, BlogList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogList.as_view(), name='post-list'),
    path('<int:pk>/', BlogDetail.as_view(), name='post-detail'),
]
