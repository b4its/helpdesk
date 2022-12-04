from django.shortcuts import render, redirect
from .forms import BioRegistration
from .models import Biodata
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# function untuk menambahkan

@login_required
def tambah_informasi_user(request):
  if request.method == 'POST':
   fm = BioRegistration(request.POST)
   if fm.is_valid(): 
     us = fm.cleaned_data['user']
     hp = fm.cleaned_data['email']
     alm = fm.cleaned_data['alamat']
     reg = Biodata(user=us,email=hp, alamat=alm)
     reg.save()
     fm = BioRegistration()
  else:
   fm = BioRegistration()
  biod = Biodata.objects.all()
  return render(request, 'tambah_list_user.html', {'form':fm})

@login_required
def update_bio(request, id):
  if request.method == 'POST':
    pi = Biodata.objects.get(pk=id)
    fm = BioRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
      return redirect('list_user')
  else:
    pi = Biodata.objects.get(pk=id)
    fm = BioRegistration(instance=pi)
    return render(request, 'update_biodata.html', {'form':fm})

@login_required
def search_biodata(request):
    if request.method == "POST":
        cari = request.POST['cari']
        hasil = Biodata.objects.filter(user__username__contains=cari)
        return render(request, "search_biodata.html",
        {'cari':cari,'hasil':hasil})
    else:
        return render(request, "search_biodata.html",
        {})
        
@login_required        
def biodata(request):
    posts = Biodata.objects.all()
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

