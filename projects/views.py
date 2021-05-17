from django.shortcuts import render
from .models import ProjectName
from django.shortcuts import get_object_or_404


def projects_index(request):
    posts = ProjectName.objects.all()
    return render(request, 'projects/index.html', {'posts':posts})


def post(request, id):
    post = get_object_or_404(ProjectName, pk=id)
    return render(request, 'projects/post.html', {'object': post})
