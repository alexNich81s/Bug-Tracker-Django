from django.urls import path
from .views import bug_detail
urlpatterns = [
    path('<int:id>', bug_detail, name="bug_detail")
]