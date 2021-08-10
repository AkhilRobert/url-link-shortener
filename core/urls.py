from django.urls import path
from .views import HomeView, ShrinkView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<str:id>", ShrinkView.as_view(), name="shrink")
]
