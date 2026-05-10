from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)

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

class ThemeSettings(models.Model):
    PATTERN_CHOICES = [
        ('none', 'Solid Color'),
        ('dots', 'Dotted Grid'),
        ('grid', 'Square Grid'),
    ]

    name = models.CharField(max_length=50, default="Default Dark")
    bg_color = models.CharField(max_length=7, default="#0c0c0e")
    accent_color = models.CharField(max_length=7, default="#a78bfa")
    card_color = models.CharField(max_length=7, default="#161619")
    text_color = models.CharField(max_length=7, default="#f4f4f5")
    
    bg_pattern = models.CharField(max_length=10, choices=PATTERN_CHOICES, default='dots')
    bg_pattern_color = models.CharField(max_length=7, default="#ffffff", help_text="Color for the grid/dots")
    bg_pattern_opacity = models.FloatField(default=0.05, help_text="Opacity (0.0 to 1.0)")
    
    bg_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    bg_image_blur = models.IntegerField(default=0, help_text="Blur in pixels")
    bg_image_brightness = models.FloatField(default=1.0, help_text="Brightness (e.g., 0.5 for dark)")
    
    is_active = models.BooleanField(default=True)
    
    # Animation Controls
    anim_speed = models.FloatField(default=0.6, help_text="Animation duration in seconds (e.g., 0.6)")
    typing_speed = models.IntegerField(default=150, help_text="Typing speed in milliseconds (e.g., 150)")

    class Meta:
        verbose_name_plural = "Theme Settings"

    def __str__(self):
        return self.name
