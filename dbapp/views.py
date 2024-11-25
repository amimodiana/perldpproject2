from django.shortcuts import render
# from .models import Blogpost

# creat your views here

def blog_list(request):

    posts=Blogpost.objects.all()
    return render(request,'blog_list.html',{'posts':posts})
def blog_detail(request,id):
    post=get_object or 404(Blogpost, id=id)
    retun render(request,'blog_details.html',{'post':post})




