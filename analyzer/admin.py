from django.contrib import admin
from .models import SequenceAnalysis

@admin.register(SequenceAnalysis)
class SequenceAnalysisAdmin(admin.ModelAdmin):
    # 'name' does not exist on SequenceAnalysis model; use existing fields instead.
    list_display = ('id', 'sequence_type', 'created_at')
    # allow searching by sequence content
    search_fields = ('original_sequence',)
    list_filter = ('created_at', 'sequence_type')
    ordering = ('-created_at',)
    show_facets = admin.ShowFacets.ALWAYS