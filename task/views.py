from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import *
from .models import *


def index(request):
    user = request.user
    if user.is_authenticated:
        images = Record.objects.filter(user_login=user.username)
        form = UploadRecordForm
        if request.method == "POST":
            form = UploadRecordForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user_login = user.username
                if post.image.size >= 2097152:
                    return
                post.save()
        else:
            form = UploadRecordForm
        return render(
            request,
            "index.html",
            locals()
        )
    else:
        form = False
        return render(
            request,
            'index.html',
            context=locals()
        )


def personal(request):
    if request.user.is_authenticated:
        images = Record.objects.filter(user_login=request.user.username)
        return render(
            request,
            "personal.html",
            locals()
        )
    else:
        return redirect("/accounts/login/")


def change_image(request, id):
    record = Record.objects.get(id=id)
    form = ChangePhotoForm

    if request.method == "POST":
        form = ChangePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            if image.size >= 2097152:
                return
            record.image = image
            record.save()
            return redirect("/change/id/")
    else:
        form = UploadRecordForm
    return render(
        request,
        'post-detail.html',
        locals()
    )


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = "/accounts/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)


def redirect_view(request):
    return redirect('/')
