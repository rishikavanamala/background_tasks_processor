import requests
from django.core.mail import send_mail
from .models import BackgroundTask
import time
import os
from django.conf import settings
import requests
from .models import BackgroundTask

def send_email_task(task_id):
    task = BackgroundTask.objects.get(id=task_id)

    try:
        task.status = "RUNNING"
        task.save()

        time.sleep(5)  # simulate delay

        send_mail(
            subject="Background Task Email",
            message="This email was sent in background.",
            from_email=None,
            recipient_list=["test@example.com"],
        )

        task.status = "SUCCESS"
        task.save()

    except Exception as e:
        task.status = "FAILED"
        task.error_message = str(e)
        task.save()

MAX_RETRIES = 3

def download_file_task(task_id, file_url):
    task = BackgroundTask.objects.get(id=task_id)

    try:
        task.status = "RUNNING"
        task.save()

        response = requests.get(file_url, timeout=5)
        response.raise_for_status()

        download_dir = os.path.join(settings.BASE_DIR, "media", "downloads")
        os.makedirs(download_dir, exist_ok=True)

        file_path = os.path.join(download_dir, f"task_{task_id}.pdf")

        with open(file_path, "wb") as f:
            f.write(response.content)

        task.file_path = file_path
        task.status = "SUCCESS"
        task.save()

    except Exception as e:
        task.retry_count += 1
        task.error_message = str(e)

        if task.retry_count >= MAX_RETRIES:
            task.status = "FAILED"
        else:
            task.status = "PENDING"
            # retry again
            download_file_task(task_id, file_url)

        task.save()