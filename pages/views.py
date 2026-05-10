from django.shortcuts import render
from projects.models import Project, SkillCategory, HeroContent, AboutContent, Stat, SocialLink, ThemeSettings, Reference

def get_base_context(request):
    return {
        'social_links': SocialLink.objects.all(),
        'theme': ThemeSettings.objects.filter(is_active=True).first()
    }

def home(request):
    all_projects = Project.objects.all()
    project_count = all_projects.count()
    skill_categories = SkillCategory.objects.all().prefetch_related('skills')
    hero = HeroContent.objects.filter(is_active=True).first()
    stats = Stat.objects.all()
    reference_count = Reference.objects.count()
    
    # Dynamically update stats
    for stat in stats:
        label_lower = stat.label.lower()
        if 'project' in label_lower:
            stat.value = f"{project_count}+" if project_count > 0 else "0"
        elif 'client' in label_lower or 'reference' in label_lower:
            stat.value = f"{reference_count}+" if reference_count > 0 else "0"

    context = get_base_context(request)
    context.update({
        'featured_projects': all_projects,
        'skill_categories': skill_categories,
        'hero': hero,
        'stats': stats,
    })
    return render(request, 'pages/home.html', context)

def about(request):
    about_content = AboutContent.objects.filter(is_active=True).first()
    context = get_base_context(request)
    context.update({
        'about': about_content
    })
    return render(request, 'pages/about.html', context)

def references_view(request):
    references = Reference.objects.all()
    context = get_base_context(request)
    context.update({
        'references': references
    })
    return render(request, 'pages/references.html', context)

def admin_preview_view(request):
    context = get_base_context(request)
    return render(request, 'pages/admin_preview.html', context)
