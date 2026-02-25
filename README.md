## Bioinfo Sequence Analyzer

This repository contains a small Django project for basic bioinformatics sequence analysis. It provides:
- A **web UI** where you can paste a DNA or RNA sequence and see:
  - Validation of the sequence (allowed characters depending on DNA/RNA)
  - DNA → RNA **transcription**
  - RNA → protein **translation** (codon-based)
  - **GC content** percentage
- A simple **JSON API** endpoint that exposes the same analysis programmatically.

### Project structure

- `manage.py` – standard Django management script.
- `bioinfo/` – main Django project (settings, URLs, WSGI/ASGI).
- `analyzer/` – application containing:
  - `bioinfo.py` – core analysis functions (transcription, translation, GC%, validation).
  - `views.py` – web view (`web_analyze`) and API view (`api_analyze`).
  - `models.py` – `SequenceAnalysis` model used to persist analyses.
  - `templates/analyzer/` – HTML templates for the form and results.

### Requirements

This is a standard Django project. You will need:

- Python 3.9+ (or any recent 3.x supported by your Django version)
- Django (e.g. `django>=4.0`)

If you already have a `venv` with Django installed you can skip the installation step below.

### Setup and installation

1. **Clone the repository** (or download the source code).
2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Linux/macOS
   # .venv\Scripts\activate  # on Windows PowerShell
   ```

3. **Install dependencies** (at minimum Django):

   ```bash
   pip install "django>=4.0"
   ```

4. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. Open your browser at `http://127.0.0.1:8000/` (or the URL configured in `bioinfo/urls.py`) to use the web interface.

### Usage

- **Web UI**
  - Navigate to the main page rendered by `web_analyze`.
  - Enter your DNA or RNA sequence and select the type.
  - Submit to see transcription, translation, and GC%.

- **API**
  - Send a POST request with a JSON body to the API endpoint (see `analyzer/urls.py` for the exact path), for example:

    ```bash
    curl -X POST \
      -H "Content-Type: application/json" \
      -d '{"sequence": "ATGCGT", "type": "DNA"}' \
      http://127.0.0.1:8000/api/analyze/
    ```

  - The response will include:
    - `sequence` – cleaned/validated sequence.
    - `type` – DNA or RNA.
    - `rna` – transcribed RNA (for DNA input).
    - `protein` – translated amino-acid sequence.
    - `gc_percentage` – GC content (%).

### Tests

There is a placeholder `tests.py` in the `analyzer` app. You can add Django tests there and run:

```bash
python manage.py test
```

### License

Add your preferred license here (e.g. MIT, Apache-2.0).

