import os
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project

@receiver(post_save, sender=Project)
def optimize_project_image(sender, instance, created, **kwargs):
    if instance.image:
        image_path = instance.image.path
        
        # Open the image using Pillow
        with Image.open(image_path) as img:
            # Check if resize is needed
            max_width = 1200
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int(float(img.height) * float(ratio))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert and save as WebP
            base, ext = os.path.splitext(image_path)
            new_path = f"{base}.webp"
            
            img.save(new_path, "WEBP", quality=85)
            
            # Update the model instance to use the new path if it was converted
            if ext.lower() != '.webp':
                # Delete old file
                if os.path.exists(image_path):
                    os.remove(image_path)
                
                # Update path in DB without triggering another save signal
                instance.image.name = instance.image.name.rsplit('.', 1)[0] + '.webp'
                instance.save(update_fields=['image'])
