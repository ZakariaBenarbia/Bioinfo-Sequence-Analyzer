from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from .bioinfo import transcription, translation, calculate_gc_percentage, validate_sequence
from .models import SequenceAnalysis


def web_analyze(request):
    """Web view: render form and show results (template-based)."""
    if request.method == 'POST':
        sequence = request.POST.get('sequence', '')
        seq_type = request.POST.get('type', 'DNA')

        valid, res = validate_sequence(sequence, seq_type)
        if not valid:
            return render(request, 'analyzer/form.html', {'error': res, 'sequence': sequence, 'type': seq_type})

        cleaned = res
        if seq_type == 'DNA':
            rna = transcription(cleaned)
        else:
            rna = cleaned

        protein = translation(rna)
        gc = calculate_gc_percentage(cleaned)

        context = {
            'sequence': cleaned,
            'type': seq_type,
            'rna': rna,
            'protein': protein,
            'gc_percentage': gc,
        }
        # Persist the analysis to the database
        try:
            SequenceAnalysis.objects.create(
                original_sequence=cleaned,
                sequence_type=seq_type,
                transcription=rna,
                translation=protein,
                gc_percentage=gc,
            )
        except Exception:
            # Don't break the web UI if DB write fails; continue to show results
            pass
        return render(request, 'analyzer/result.html', context)
    else:
        return render(request, 'analyzer/form.html')


@csrf_exempt
def api_analyze(request):
    """API view: accept JSON POST and return JSON results."""
    if request.method != 'POST':
        return HttpResponseBadRequest('Use POST with JSON payload')

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')

    sequence = payload.get('sequence', '')
    seq_type = payload.get('type', 'DNA')

    valid, res = validate_sequence(sequence, seq_type)
    if not valid:
        return JsonResponse({'error': res}, status=400)

    cleaned = res
    if seq_type == 'DNA':
        rna = transcription(cleaned)
    else:
        rna = cleaned

    protein = translation(rna)
    gc = calculate_gc_percentage(cleaned)
    # Persist the analysis to the database for API requests as well
    try:
        SequenceAnalysis.objects.create(
            original_sequence=cleaned,
            sequence_type=seq_type,
            transcription=rna,
            translation=protein,
            gc_percentage=gc,
        )
    except Exception:
        # For API keep behavior simple; don't crash on DB write failure
        pass

    return JsonResponse({
        'sequence': cleaned,
        'type': seq_type,
        'rna': rna,
        'protein': protein,
        'gc_percentage': gc,
    })
