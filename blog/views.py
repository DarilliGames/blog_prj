from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def get_main(request):
    blogs = Post.objects.all()
    return render(request, "blog/index.html", {"blogs":blogs})
    
def get_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    blog.views +=1
    blog.save()
    return render(request, "blog/blog.html", {"blog" : blog})

    
def write_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("mainblog")
    else:
        form = PostForm()
        return render(request, "blog/writeblog.html", {"form": form})

def edit_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=blog)
            if form.is_valid():
                form.save()
                return redirect("mainblog")
        form = PostForm(instance=blog)
        return render(request, "blog/writeblog.html", {"form" : form})
    else:
        return redirect("mainblog")

def delete_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user:
        return render(request, "blog/delete.html", {"blog" : blog})
    else:
        return redirect("mainblog")

def delete_confirm(request, id):
    blog = get_object_or_404(Post, pk=id)
    if blog.author == request.user:
        print(blog.author)
        print(request.user)
        blog.delete()
        return redirect("mainblog")
    return redirect("mainblog")

    