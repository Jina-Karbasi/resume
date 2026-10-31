from django.urls import path
from core.views import  *



urlpatterns = [
    path("", index_view, name= "index"),
    path("contact/", contact_view, name= "contact"),
    path("projects/", projects_view, name= "projects"),
    path("resume/", resume_view, name= "resume"),      
]