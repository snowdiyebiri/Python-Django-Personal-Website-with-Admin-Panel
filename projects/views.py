from django.shortcuts import render
from .models import Project
from django.db.models import Q

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)

def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Project.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(technology__icontains=query)
        ).distinct()
    
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'projects/search_results.html', context)
