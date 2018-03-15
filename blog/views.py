from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def get_main(request):
    blogs = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blog/index.html", {"blogs":blogs})
    
def get_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    blog.views +=1
    blog.save()
    return render(request, "blog/blog.html", {"blog" : blog})

@login_required()  
def write_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'publish' in request.POST:
                post.publish()
                print(post.published_date)
            post.save()
            return redirect("mainblog")
    else:
        form = PostForm()
        return render(request, "blog/writeblog.html", {"form": form})

@login_required()
def edit_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user or request.user.is_staff:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=blog)
            if form.is_valid():
                form.save()
                return redirect("mainblog")
        form = PostForm(instance=blog)
        return render(request, "blog/writeblog.html", {"form" : form})
    else:
        return redirect("mainblog")

@login_required() 
def delete_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user:
        return render(request, "blog/delete.html", {"blog" : blog})
    else:
        return redirect("mainblog")

@login_required() 
def delete_confirm(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user:
        blog.delete()
        return redirect("yourprofile")
    return redirect("mainblog")

@login_required() 
def publish(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user:
        blog.publish()
        blog.save()
    print(blog.published_date)
    return redirect("yourprofile")
    
