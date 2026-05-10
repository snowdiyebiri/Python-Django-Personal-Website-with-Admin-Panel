import os
import psutil
from django import template
from django.db import connection
from projects.models import Project, Skill, Stat

register = template.Library()

from contact.models import Message

@register.simple_tag
def get_performance_metrics():
    # System Metrics
    cpu_usage = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    
    # Database Metrics
    db_size = 0
    if connection.vendor == 'sqlite':
        db_path = connection.settings_dict['NAME']
        if os.path.exists(db_path):
            db_size = os.path.getsize(db_path) / (1024 * 1024)  # Size in MB

    # Content Metrics
    project_count = Project.objects.count()
    skill_count = Skill.objects.count()
    stat_count = Stat.objects.count()
    
    # New: Latest Messages
    latest_messages = Message.objects.all()[:5]
    unread_count = Message.objects.filter(is_read=False).count()
    
    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'db_size': round(db_size, 2),
        'project_count': project_count,
        'skill_count': skill_count,
        'stat_count': stat_count,
        'latest_messages': latest_messages,
        'unread_count': unread_count,
    }
