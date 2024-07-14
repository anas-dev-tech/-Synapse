from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users_online = models.ManyToManyField(
        User,
        related_name='online_in_groups',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    


class GroupMessage(models.Model):
    group = models.ForeignKey(
        ChatGroup,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    ) 

    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"Message by {self.author} in {self.group.group_name}"

    