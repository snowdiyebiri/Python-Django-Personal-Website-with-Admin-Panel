from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Message

@staff_member_required
def latest_messages_api(request):
    messages = Message.objects.all()[:5]
    data = []
    for msg in messages:
        data.append({
            'name': msg.name,
            'email': msg.email,
            'content': msg.content[:50] + '...' if len(msg.content) > 50 else msg.content,
            'created_at': msg.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'is_read': msg.is_read,
        })
    return JsonResponse({'messages': data, 'unread_count': Message.objects.filter(is_read=False).count()})
