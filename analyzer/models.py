from django.db import models

class SequenceAnalysis(models.Model):
    NUCLEOTIDE_CHOICES = [
        ('DNA', 'ADN'),
        ('RNA', 'ARN'),
    ]
    
    original_sequence = models.TextField()
    sequence_type = models.CharField(max_length=3, choices=NUCLEOTIDE_CHOICES)
    transcription = models.TextField(blank=True)
    translation = models.TextField(blank=True)
    gc_percentage = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Sequence analysis - {self.created_at}"
