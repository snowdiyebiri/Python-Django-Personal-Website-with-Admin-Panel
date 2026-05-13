from django.contrib import admin
from django import forms
from .models import Project, SkillCategory, Skill, HeroContent, AboutContent, Stat, SocialLink, ThemeSettings, Reference, SiteConfiguration

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
            # Dark Mode
            'bg_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'accent_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'card_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'text_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'text_secondary_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            
            # Light Mode
            'light_bg_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'light_accent_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'light_card_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'light_text_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'light_text_secondary_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            'light_bg_pattern_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            
            'bg_pattern_color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px;'}),
            
            # Slider Widgets
            'bg_pattern_opacity': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '1', 'step': '0.01'}),
            'bg_image_blur': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '50', 'step': '1'}),
            'bg_image_brightness': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '2', 'step': '0.05'}),
            'anim_speed': forms.NumberInput(attrs={'type': 'range', 'min': '0.1', 'max': '2', 'step': '0.1'}),
        }

class ThemeSettingsAdmin(admin.ModelAdmin):
    form = ThemeSettingsForm
    fieldsets = (
        (None, {
            'fields': ('name', 'is_active')
        }),
        ('Dark Mode Colors', {
            'fields': ('bg_color', 'accent_color', 'card_color', 'text_color', 'text_secondary_color')
        }),
        ('Light Mode Colors', {
            'fields': ('light_bg_color', 'light_accent_color', 'light_card_color', 'light_text_color', 'light_text_secondary_color', 'light_bg_pattern_color')
        }),
        ('Background Pattern', {
            'fields': ('bg_pattern', 'bg_pattern_color', 'bg_pattern_opacity')
        }),
        ('Background Image', {
            'fields': ('bg_image', 'bg_image_blur', 'bg_image_brightness')
        }),
        ('Brand Elements', {
            'fields': ('logo', 'favicon')
        }),
        ('Animations', {
            'fields': ('anim_speed', 'typing_speed')
        }),
    )

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'company', 'testimonial')

admin.site.register(Project)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(HeroContent)
@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_editable = ('is_active',)
admin.site.register(Stat)
admin.site.register(SocialLink)
admin.site.register(ThemeSettings, ThemeSettingsAdmin)
class SiteConfigurationForm(forms.ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = '__all__'
        widgets = {
            'container_width': forms.NumberInput(attrs={'type': 'range', 'min': '800', 'max': '2000', 'step': '10'}),
            'grid_column_width': forms.NumberInput(attrs={'type': 'range', 'min': '200', 'max': '800', 'step': '10'}),
            'card_border_radius': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'step': '1'}),
            'glass_blur': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '50', 'step': '1'}),
            'nav_padding_y': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '5', 'step': '0.1'}),
            'section_padding_y': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '10', 'step': '0.5'}),
            'hero_gap': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '5', 'step': '0.1'}),
            'container_padding_top': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '10', 'step': '0.5'}),
        }

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    form = SiteConfigurationForm
    list_display = ('__str__',)
    fieldsets = (
        ('Layout & Spacing', {
            'fields': ('container_width', 'grid_column_width', 'card_border_radius', 'glass_blur', 'nav_padding_y', 'section_padding_y', 'hero_gap', 'container_padding_top')
        }),
        ('Branding & Navigation', {
            'fields': ('logo_part_1', 'logo_part_2', 'nav_home', 'nav_projects', 'nav_about', 'nav_references', 'nav_admin', 'nav_contact')
        }),
        ('Section Titles & Content', {
            'fields': ('projects_title_prefix', 'projects_title_highlight', 'contact_title_prefix', 'contact_title_highlight', 'contact_description', 'references_title_prefix', 'references_title_highlight', 'skills_title_prefix', 'skills_title_highlight', 'skills_sub_label')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'contact_location', 'contact_social_text')
        }),
        ('Footer', {
            'fields': ('footer_copyright', 'footer_tagline')
        }),
    )

