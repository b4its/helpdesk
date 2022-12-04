from django.shortcuts import redirect, render, HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import MyfileUploadForm, TeknisiFileUploadForm
from .models import FileUpload
from textwrap import wrap
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def index(request):
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            nama = form.cleaned_data['file_name']
            pembahasan = form.cleaned_data['pembahasan']
            the_files = form.cleaned_data['files_data']
            FileUpload(file_name=nama,pembahasan=pembahasan, my_file=the_files).save()
            return redirect('tampilan_gambar')
        else:
            return HttpResponse('error')
    else:
        context = {
            'form':MyfileUploadForm()
        }      
        return render(request, 'menambahkan_gambar.html', context)
    
@login_required
def show_file(request):
    #pagination
    posts = FileUpload.objects.all().order_by('-date_posted')
    p = Paginator(posts, 2) 
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

    return render(request, 'menampilkan_gambar.html', context)

@login_required
def update_informasi_keluhan(request, id):
  if request.method == 'POST':
    print("tes")
    pi = FileUpload.objects.get(pk=id)
    fm = TeknisiFileUploadForm(request.POST,request.FILES, instance=pi)
    if fm.is_valid():
      fm.save()
      return redirect('tampilan_gambar')
  else:
    pi = FileUpload.objects.get(pk=id)
    fm = TeknisiFileUploadForm(instance=pi) 
  return render(request, 'update_file.html', {'form':fm})

def search(request):
    if request.method == "POST":
        pencarian = request.POST['pencarian']
        hasil = FileUpload.objects.filter(file_name__contains=pencarian)
        return render(request, "search.html",
        {'pencarian':pencarian,'hasil':hasil})
    else:
        return render(request, "search.html",
        {})




    

