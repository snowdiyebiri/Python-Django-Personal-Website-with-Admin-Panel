from django.shortcuts import render
from projects.models import Project, SkillCategory, HeroContent, AboutContent, Stat, SocialLink, ThemeSettings

def get_base_context(request):
    return {
        'social_links': SocialLink.objects.all(),
        'theme': ThemeSettings.objects.filter(is_active=True).first()
    }

def home(request):
    all_projects = Project.objects.all()
    skill_categories = SkillCategory.objects.all().prefetch_related('skills')
    hero = HeroContent.objects.filter(is_active=True).first()
    stats = Stat.objects.all()
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
