from django.shortcuts import render


# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# function untuk menambahkan


def dashboard(request):
    return render(request, "dashboard.html")

        
