# src/utils/data_utils.py

def parse_triplets(strings):
    """Parse a list of triplet strings into separate lists of subjects, relations, and objects."""
    subjects, relations, objects = [], [], []
    for string in strings:
        s, r, o = parse_triplet(string)
        subjects.append(s)
        relations.append(r)
        objects.append(o)
    return subjects, relations, objects

def parse_triplet(string):
    """Parse a single triplet string into subject, relation, and object."""
    parts = string.split(':')
    return [part.lower().strip() for part in parts]

def get_unique_elements(lst):
    """Get unique elements from a list while preserving order."""
    return list(dict.fromkeys(lst))
