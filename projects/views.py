from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, ThemeSettings
from django.db.models import Q
from pages.views import get_base_context

def project_index(request):
    projects = Project.objects.all()
    context = get_base_context(request)
    context.update({
        'projects': projects
    })
    return render(request, 'projects/project_index.html', context)

def project_detail(request, slug):
    try:
        project = Project.objects.get(slug=slug)
        context = get_base_context(request)
        context.update({
            'project': project
        })
        return render(request, 'projects/project_detail.html', context)
    except Project.DoesNotExist:
        from django.http import Http404
        raise Http404("Project does not exist")

def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Project.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(technology__icontains=query)
        ).distinct()
    
    context = get_base_context(request)
    context.update({
        'query': query,
        'results': results,
    })
    return render(request, 'projects/search_results.html', context)

def activate_theme(request, theme_id):
    ThemeSettings.objects.all().update(is_active=False)
    theme = get_object_or_404(ThemeSettings, id=theme_id)
    theme.is_active = True
    theme.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))
