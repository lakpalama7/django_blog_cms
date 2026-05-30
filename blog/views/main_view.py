

from django.shortcuts import render, redirect, get_object_or_404
from ..models import Blogs, Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    blogs = Blogs.objects.all()
    context = {
        "blogs":blogs,
    }
    return render(request, 'main/home.html',context)

def single_blog(request, blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id)

    
    return render(request, 'main/single_blog.html', {"blog":blog})

def edit_blog(request, blog_id):

    blog = get_object_or_404(Blogs, id=blog_id)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.subtitle = request.POST.get('subtitle')
        blog.description = request.POST.get('description')

        if request.FILES.get('image'):
            blog.image = request.FILES.get('image')
        blog.save()

        return redirect('single_blog', blog_id=blog_id)
    
    elif blog.author == request.user:

        context = {
            'blog':blog
        }
        return render(request, 'main/edit_blog.html', context)
    else:
        return redirect('single_blog', blog_id=blog.id)
    
    


@login_required
def create_blog(request):

    if request.method == 'POST':
   
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        blog = Blogs(title=title, subtitle=subtitle, description=description,image=image, author=request.user)
        blog.save()
        return redirect('home')

    return render(request, 'main/create_blog.html')

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    if blog.author == request.user:
        blog.delete()
        return redirect('home')
    else:
        return redirect('single_blog', blog_id=blog.id)
   

def about_blog(request):
    return render(request,'main/about_blog.html')

def contact_blog(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name == '' or email == '' or subject == '' or message == '':
            messages.error(request,"Fill the required all content")
        else:
            contact = Contact(name=name,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,"message sent successfully")
        
    return render(request,'main/contact_blog.html')