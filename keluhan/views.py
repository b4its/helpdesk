from django.shortcuts import render, redirect, HttpResponseRedirect
from input.models import Keluhan
from .forms import KeluhanForms, TeknisiKeluhan
from .models import List_keluhan 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# function untuk menambahkan

@login_required
def keluhan_teknisi(request):
  if request.method == 'POST':
   fm = KeluhanForms(request.POST)
   if fm.is_valid(): 
     jd = fm.cleaned_data['judul']
     pb = fm.cleaned_data['pembahasan']
     reg = List_keluhan(judul=jd, pembahasan=pb).save()
     reg.save()
     fm = KeluhanForms()
  else:
   fm = KeluhanForms()
   prob = List_keluhan.objects.all().order_by('-date_posted')
   p = Paginator(prob, 3) 
   page_number = request.GET.get('page')
   try:
        teknisi = p.get_page(page_number)  # returns the desired page object
   except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        teknisi = p.page(1)
   except EmptyPage:
        # if page is empty then return last page
        teknisi = p.page(p.num_pages)
    # sending the page object to index.html
  
   context = { 
        'teknisi': teknisi
        }
   return render(request, 'keluhan.html',context)

@login_required
def keluhan_pengguna(request):
  if request.method == 'POST':
   fm = KeluhanForms(request.POST)
   if fm.is_valid(): 
     jd = fm.cleaned_data['judul']
     pb = fm.cleaned_data['pembahasan']
     reg = List_keluhan(judul=jd, pembahasan=pb).save()
     reg.save()
     fm = KeluhanForms()
  else:
   fm = KeluhanForms()
   prob = List_keluhan.objects.filter(user=request.user)
   p = Paginator(prob, 3) 
   page_number = request.GET.get('page')
   try:
        pengguna = p.get_page(page_number)  # returns the desired page object
   except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        pengguna = p.page(1)
   except EmptyPage:
        # if page is empty then return last page
        pengguna = p.page(p.num_pages)
    # sending the page object to index.html
  
   context = { 
        'pengguna': pengguna
        }
   return render(request, 'keluhanmu.html',context)

@login_required
def tambahkan_keluhan(request):
  if request.method == 'POST':
   problem_forms = KeluhanForms(request.POST)
   if problem_forms.is_valid(): 
     post = problem_forms.save(commit=False)
     post.user = request.user
     post.save()
     return redirect('tambah_gambar')
  else:
   problem_forms = KeluhanForms()
   prob = List_keluhan.objects.all()
  return render(request, 'tambahkan_keluhan.html', {'form':problem_forms})

@login_required
def update_keluhan(request, id):
  if request.method == 'POST':
    pi = List_keluhan.objects.get(pk=id)
    fm = TeknisiKeluhan(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
      return redirect('problem')
  else:
    pi = List_keluhan.objects.get(pk=id)
    fm = TeknisiKeluhan(instance=pi)
  return render(request, 'update_keluhan.html', {'form':fm})

@login_required
def search_teknisi(request):
    if request.method == "POST":
        pencarian = request.POST['pencarian']
        hasil = List_keluhan.objects.filter(teknisi__username__contains=pencarian)
              
        return render(request, "search_keluhan.html",
        {'pencarian':pencarian,'hasil':hasil})
    else:
        return render(request, "search_keluhan.html",
        {})
