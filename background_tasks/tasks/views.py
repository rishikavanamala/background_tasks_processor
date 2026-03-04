import threading
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import BackgroundTask
from .background import send_email_task, download_file_task
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import BackgroundTask
import threading
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from .models import BackgroundTask
from .background import send_email_task, download_file_task

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@require_POST
def send_email_api(request):
    task = BackgroundTask.objects.create(
        name="Send Email"
    )

    thread = threading.Thread(
        target=send_email_task,
        args=(task.id,),
        daemon=True
    )
    thread.start()

    return JsonResponse({
        "task_id": task.id,
        "status": task.status
    })

@csrf_exempt
@require_POST
def download_file_api(request):
    task = BackgroundTask.objects.create(name="Download File")

    file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

    thread = threading.Thread(
        target=download_file_task,
        args=(task.id, file_url),
        daemon=True
    )
    thread.start()

    return JsonResponse({
        "task_id": task.id,
        "status": task.status
    })
    
    
    
@require_GET
def task_status_api(request, task_id):
    try:
        task = BackgroundTask.objects.get(id=task_id)

        return JsonResponse({
            "task_id": task.id,
            "task_name": task.name,
            "status": task.status,
            "error": task.error_message,
            "created_at": task.created_at,
            # "updated_at": task.updated_at,
        })

    except BackgroundTask.DoesNotExist:
        return JsonResponse(
            {"error": "Task not found"},
            status=404
        )
