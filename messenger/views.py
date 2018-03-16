from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import Message
from .forms import MessageForm



def get_index(request):
    return render(request, "messenger/index.html")

def inbox(request):
    return render(request, "messenger/index.html")
    
def sent(request):
    return render(request, "messenger/sent.html")


@login_required(login_url='login')
def get_mail(request, id):
    mail = get_object_or_404(Message, pk=id)
    if (request.user == mail.sender):
        mail.read = True
        mail.save()
        return render(request, "messenger/mail.html", {"mail" : mail})
    elif (request.user == mail.recipient):
        return render(request, "messenger/mail.html", {"mail" : mail})
    else:
        return redirect("index")

# def get_mail(request, id):
#     mail = get_object_or_404(Message, pk=id)
#     if (request.user == mail.sender):
#         print(mail.sender)
#         print(request.user)
#         return render(request, "messenger/mail.html", {"mail" : mail})
#     elif (request.user == mail.recipient):
#         return render(request, "messenger/mail.html", {"mail" : mail})
#     else:
#         return render(request, "messenger/mail.html", {"mail" : mail})

def write_mail(request):
    form = MessageForm()
    return render(request, "messenger/compose.html", {"form" : form})

def send(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
    return redirect("inbox")