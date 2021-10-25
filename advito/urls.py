from django.urls import path
from django.views.generic import TemplateView

from .views import (
    AnnouncementView, PostDetailView, PostCreateView, EditView, PostDelete, CategoryView, Category_choiseView, IndexView
)
from .urls_auth import urlpatterns as auth_patterns

app_name ='advito'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('announcement/', AnnouncementView.as_view(), name="announcement"),
    path('announcement/<int:post_id>/', PostDetailView.as_view(), name="post_detail"),
    path('announcement/create/', PostCreateView.as_view(), name="post_create"),
    path('announcement/<int:post_id>/edit', EditView.as_view(), name="post_edit"),
    path('announcement/<int:post_id>/delete', PostDelete.as_view(), name="post_delete"),
    path('announcement/<int:post_id>/delete-success', TemplateView.as_view(template_name='advito/delete_success.html'), name="post_delete_success"),
    path('category/', CategoryView.as_view(), name="category"),
    path('category/<int:category_id>/', Category_choiseView.as_view(), name="choise_category")
]

urlpatterns += auth_patterns