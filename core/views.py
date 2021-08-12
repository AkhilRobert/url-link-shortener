from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .forms import ShrinkURLForm
from .models import CoreModel


class HomeView(View):
    def get(self, request):
        return render(request, "core/index.html", {"form": ShrinkURLForm})

    def post(self, request):
        form = ShrinkURLForm(request.POST)
        if form.is_valid():
            val = form.save()
            messages.success(
                request, f"http://{request.get_host()}/{val.shrink_id}")
        else:
            messages.error(request, "Invalid URL")
        return redirect(reverse("home"))


class ShrinkView(View):
    def get(self, _, id):
        qs = CoreModel.objects.filter(shrink_id=id).first()
        if qs is None:
            return redirect(reverse("home"))
        return redirect(qs.original_url)
