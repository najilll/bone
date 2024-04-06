from .models import Services

def services(request):
    return {'service': Services.objects.filter(is_active=True)}