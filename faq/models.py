from django.db import models

class FAQ(models.Model):
    """Model definition for FAQ."""
    faq_question = models.TextField()
    answer = models.TextField()
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        """Meta definition for FAQ."""

        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        """Unicode representation of FAQ."""
        return self.faq_question

