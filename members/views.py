from django.shortcuts import render
from members.models import Member
from .forms import RegosterForm
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
import uuid

def index(request, id=None):
    file_url = ''
    if request.method == 'POST':
        
        folder='public/storage/img/'
        
        myfile = request.FILES['image']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT 
         
        ext = myfile.name.split('.').pop()
        new_filename =  str(uuid.uuid4())+'.'+ ext
        
        fs.save(new_filename, myfile)
        
        form = RegosterForm(request.POST)
        if form.is_valid():
            member = Member(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], avatar=new_filename)
            member.save()
            
            
    edit = {}
    if id and id > 0:
        objs = Member.objects.filter(pk=id)
        if len(objs) >= 1:
            edit = objs[0]
            
            
    members = Member.objects.all().order_by('id')
    
    return render(request, 'index.html', {'members':members, 'edit':edit, 'file_url':file_url});













@require_http_methods(["POST", "GET"])
def update(request, id=None):
    if request.method == 'POST':
        
        folder='public/storage/img/'
        
        myfile = request.FILES['image']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
        
        ext = myfile.name.split('.').pop()
        new_filename =  str(uuid.uuid4())+'.'+ ext
        
        fs.save(new_filename, myfile)
        
        Member.objects.filter(pk=id).update(name=request.POST['name'],email=request.POST['email'],phone=request.POST['phone'], avatar=new_filename)
        return redirect(request.META.get('HTTP_REFERER'))
    
    else:
        Member.objects.filter(pk=id).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    