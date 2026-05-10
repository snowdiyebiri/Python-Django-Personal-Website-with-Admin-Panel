from django.contrib import admin
from django import forms
from .models import Project, SkillCategory, Skill, HeroContent, AboutContent, Stat, SocialLink, ThemeSettings, Reference

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3

class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ('name', 'order')

class ThemeSettingsForm(forms.ModelForm):
    class Meta:
        model = ThemeSettings
        fields = '__all__'
        widgets = {
            'bg_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'accent_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'card_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'text_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'bg_pattern_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
        }

class ThemeSettingsAdmin(admin.ModelAdmin):
    form = ThemeSettingsForm

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'company', 'testimonial')

admin.site.register(Project)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(HeroContent)
admin.site.register(AboutContent)
admin.site.register(Stat)
admin.site.register(SocialLink)
admin.site.register(ThemeSettings, ThemeSettingsAdmin)
