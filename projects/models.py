from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HeroContent(models.Model):
    greeting = models.CharField(max_length=50, default="Hi, I'm")
    name = models.CharField(max_length=100)
    titles = models.CharField(max_length=255, default="Software Engineer, Maker, Designer", help_text="Separate with commas for the cycling effect")
    description = models.TextField()
    primary_cta_text = models.CharField(max_length=50, default="Explore Work")
    secondary_cta_text = models.CharField(max_length=50, default="Let's Talk")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Hero Content"

    def __str__(self):
        return f"Hero for {self.name}"

class AboutContent(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    summary = models.TextField()
    biography = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    years_of_experience = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "About Content"

    def __str__(self):
        return self.title

class Stat(models.Model):
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} {self.label}"

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, blank=True, help_text="FontAwesome class e.g., fa-linkedin")
    icon_image = models.ImageField(upload_to='social_icons/', blank=True, null=True, help_text="Upload custom icon image/SVG")

    def __str__(self):
        return self.platform

class Reference(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='references/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} from {self.company}"

class ThemeSettings(models.Model):
    PATTERN_CHOICES = [
        ('none', 'Solid Color'),
        ('dots', 'Dotted Grid'),
        ('grid', 'Square Grid'),
    ]

    name = models.CharField(max_length=50, default="Default Dark")
    bg_color = models.CharField(max_length=7, default="#0c0c0e", help_text="Dark mode background color")
    accent_color = models.CharField(max_length=7, default="#a78bfa", help_text="Dark mode accent color")
    card_color = models.CharField(max_length=7, default="#161619", help_text="Dark mode card color")
    text_color = models.CharField(max_length=7, default="#f4f4f5", help_text="Dark mode primary text color")
    text_secondary_color = models.CharField(max_length=7, default="#a1a1aa", help_text="Dark mode secondary text color")
    
    # Light Mode Colors
    light_bg_color = models.CharField(max_length=7, default="#fafafa", help_text="Light mode background color")
    light_accent_color = models.CharField(max_length=7, default="#8b5cf6", help_text="Light mode accent color")
    light_card_color = models.CharField(max_length=7, default="#ffffff", help_text="Light mode card color")
    light_text_color = models.CharField(max_length=7, default="#111827", help_text="Light mode primary text color")
    light_text_secondary_color = models.CharField(max_length=7, default="#4b5563", help_text="Light mode secondary text color")
    light_bg_pattern_color = models.CharField(max_length=7, default="#e5e7eb", help_text="Light mode pattern color")
    
    bg_pattern = models.CharField(max_length=10, choices=PATTERN_CHOICES, default='dots')
    bg_pattern_color = models.CharField(max_length=7, default="#ffffff", help_text="Color for the grid/dots")
    bg_pattern_opacity = models.FloatField(default=0.05, help_text="Opacity (0.0 to 1.0)")
    
    bg_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    bg_image_blur = models.IntegerField(default=0, help_text="Blur in pixels")
    bg_image_brightness = models.FloatField(default=1.0, help_text="Brightness (e.g., 0.5 for dark)")
    
    is_active = models.BooleanField(default=True)
    
    # Brand Elements
    logo = models.FileField(upload_to='logos/', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg'])], help_text="Upload a custom logo (PNG, JPG, or SVG)")
    favicon = models.FileField(upload_to='favicons/', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg', 'ico'])], help_text="Upload a custom browser icon (PNG, JPG, SVG, ICO)")
    
    # Animation Controls
    anim_speed = models.FloatField(default=0.6, help_text="Animation duration in seconds (e.g., 0.6)")
    typing_speed = models.IntegerField(default=150, help_text="Typing speed in milliseconds (e.g., 150)")

    class Meta:
        verbose_name_plural = "Theme Settings"

    def __str__(self):
        return self.name

class SiteConfiguration(models.Model):
    # Layout Settings
    container_width = models.IntegerField(default=1200, help_text="Maximum width of the website container (px)")
    grid_column_width = models.IntegerField(default=320, help_text="Minimum width of grid items (px)")
    card_border_radius = models.IntegerField(default=24, help_text="Border radius for cards (px)")
    glass_blur = models.IntegerField(default=15, help_text="Blur intensity for glass effects (px)")
    
    # Spacing Settings
    nav_padding_y = models.FloatField(default=0.8, help_text="Vertical padding for the navbar (rem)")
    section_padding_y = models.FloatField(default=3.0, help_text="Vertical padding for sections (rem)")
    hero_gap = models.FloatField(default=1.0, help_text="Gap between elements in the hero section (rem)")
    container_padding_top = models.FloatField(default=2.0, help_text="Top padding for the main container (rem)")

    logo_part_1 = models.CharField(max_length=50, default="PORT")
    logo_part_2 = models.CharField(max_length=50, default="FOLIO")
    
    # Navigation
    nav_home = models.CharField(max_length=50, default="Home")
    nav_projects = models.CharField(max_length=50, default="Projects")
    nav_about = models.CharField(max_length=50, default="About")
    nav_references = models.CharField(max_length=50, default="References")
    nav_admin = models.CharField(max_length=50, default="Admin")
    nav_contact = models.CharField(max_length=50, default="Contact")
    
    # Footer
    footer_copyright = models.CharField(max_length=100, default="SERHAT ÇAM")
    footer_tagline = models.CharField(max_length=200, default="Crafted with Django & Passion.")
    
    # Section Titles
    projects_title_prefix = models.CharField(max_length=50, default="All")
    projects_title_highlight = models.CharField(max_length=50, default="Projects")
    
    contact_title_prefix = models.CharField(max_length=50, default="Get in")
    contact_title_highlight = models.CharField(max_length=50, default="Touch")
    contact_description = models.TextField(default="Have a project in mind or just want to say hi? Drop me a message below.")
    
    references_title_prefix = models.CharField(max_length=50, default="Kind")
    references_title_highlight = models.CharField(max_length=50, default="Words")
    
    skills_title_prefix = models.CharField(max_length=50, default="Expertise")
    skills_title_highlight = models.CharField(max_length=50, default="& Tech")
    skills_sub_label = models.CharField(max_length=50, default="My Skills")

    # Contact Info
    contact_email = models.EmailField(default="hello@example.com")
    contact_phone = models.CharField(max_length=50, default="+1 (234) 567-890")
    contact_location = models.CharField(max_length=100, default="New York, USA")
    contact_social_text = models.CharField(max_length=100, default="Follow me on social media")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return "Site Configuration"
