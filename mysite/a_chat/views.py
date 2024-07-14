from django.shortcuts import render,  get_object_or_404, redirect
from .models import ChatGroup
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageCreateForm


@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, name='public-chat')
    chat_messages = chat_group.messages.all()[:30]
    form = ChatMessageCreateForm()
    
    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = chat_group
            message.author = request.user
            message.save()
            context = {
                'message': message,
                'user': request.user,
            }
            return render(request, 'a_chat/partials/chat_message_p.html', context)
        
    context = {
        'chat_messages':chat_messages,
        'form' : form,
    }
    return render(request, 'a_chat/chat.html', context)