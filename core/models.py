from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FieldUpdate(models.Model): 
    CATEGORY_CHOICES = [
        ('pest_alert', 'Pest Alert'),
        ('weather', 'Weather Observation'),
        ('crop_condition', 'Crop Condition'),
        ('fertilizer', 'Fertilizer Tip'),
        ('general', 'General Insight'),
    ]

    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='field_updates'
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.author.email})"
    
    def clean(self):
        if not self.title.strip():
            raise ValidationError("Title cannot be empty.")

        if not self.message.strip():
            raise ValidationError("Message cannot be empty.")

        categories = [c[0] for c in self.CATEGORY_CHOICES]
        if self.category not in categories:
            raise ValidationError("Invalid category selected.")

    def can_edit(self, user):
        return self.author == user