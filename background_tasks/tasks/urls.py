from django.urls import path
from .views import (
    send_email_api,
    download_file_api,
    task_status_api,
)

urlpatterns = [
    path('send-email/', send_email_api),
    path('download-file/', download_file_api),
    path('status/<int:task_id>/', task_status_api),
]
