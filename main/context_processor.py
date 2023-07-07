from .models import AppInfo

def processor(request):
    info = AppInfo.objects.get(pk=1)

    context = {
        'info':info,
    }

    return context