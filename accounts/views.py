from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("home")
    
    
def login(request):
    for k in request.GET:
        print(request.GET[k])
    
    redirect_to = request.GET.get('next', 'home')
    
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                return redirect(redirect_to)
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
        
    else:
        form = UserLoginForm()
    
    
    return render(request, 'accounts/login.html', { 'form': form })
    
    
@login_required()    
def yourprofile(request):
    return render(request, 'accounts/yourprofile.html')
    
def profile(request, id):
    person = get_object_or_404(User, pk=id)
    percheck = str(person.username)
    if person == request.user:
        return redirect('yourprofile')
    allposts = Post.objects.all()
    posts = []
    for post in allposts:
        postcheck = str(post.author)
        if postcheck == percheck:
            posts.append(post)
    return render(request, 'accounts/profile.html', {"person":person, "posts":posts})
    
     
  
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('yourprofile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})  