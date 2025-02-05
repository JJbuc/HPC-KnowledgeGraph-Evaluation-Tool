# src/utils/text_processing.py

def clean_text(text):
    """Clean text by removing special characters and normalizing spaces."""
    replacements = {
        '_': ' ',
        '`': '',
        '"': '',
        "'": ''
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return ' '.join(text.split()).lower().strip()

def split_sentences(text):
    """Split text into sentences."""
    sentences = text.split('.')
    return [s.strip() for s in sentences if s.strip()]

def normalize_triplet(subject, relation, obj):
    """Normalize a triplet by cleaning each component."""
    return (clean_text(subject),
            clean_text(relation),
            clean_text(obj))

def format_triplet(subject, relation, obj, format_type='space'):
    """Format triplet components into a string."""
    if format_type == 'space':
        return f"{subject} {relation} {obj}"
    elif format_type == 'colon':
        return f"{subject}:{relation}:{obj}"
    else:
        raise ValueError(f"Unknown format type: {format_type}")
