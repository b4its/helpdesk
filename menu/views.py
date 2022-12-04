from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# function untuk menambahkan


def help(request):
    return render(request, "bantuan.html")



@login_required
def list_user(request):
    posts = User.objects.all()
    p = Paginator(posts, 3) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    # sending the page object to index.html
    context = { 
        'page_obj': page_obj    
        }
    return render(request, 'list_user.html', context)


#def search(request):
 #   if request.method == "POST":
  #      pencarian = request.POST['pencarian']
   #     hasil = FileUpload.objects.filter(file_name__contains=pencarian)
    #    return render(request, "search.html",
     #   {'pencarian':pencarian,'hasil':hasil})
   # else:
    #    return render(request, "search.html",
     #   {})

      
        
