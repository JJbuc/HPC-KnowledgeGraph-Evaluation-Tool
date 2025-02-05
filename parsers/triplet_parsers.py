# src/parsers/triplet_parser.py

import re

def extract_triplets_regex(file_path):
    """Extract triplets using regex from file content."""
    triplet_lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Extract triplets from each line
            triplets = re.findall(r'\(([^)]+)\)', line)
            triplet_lines.extend(triplets)
            
    formatted_output = []
    for item in triplet_lines:
        parts = item.split(', ')
        if len(parts) == 3:
            subject = clean_entity(parts[0])
            relationship = clean_entity(parts[1])
            obj = clean_entity(parts[2])
            formatted_output.append(f"{subject} {relationship} {obj}")
    return formatted_output

def clean_entity(text):
    """Clean entity text by removing special characters and extra spaces."""
    text = (text.replace('`', '')
            .replace('_', ' ')
            .replace('"', '')
            .replace("'", '')
            .strip())
    return ' '.join(text.split())

def parse_triplet_string(triplet_str, separator=':'):
    """Parse a triplet string into subject, relation, object components."""
    try:
        components = triplet_str.split(separator)
        if len(components) != 3:
            raise ValueError(f"Invalid triplet format: {triplet_str}")
        subject = components[0].strip()
        relation = components[1].strip()
        obj = components[2].strip()
        return subject, relation, obj
    except Exception as e:
        print(f"Error parsing triplet {triplet_str}: {str(e)}")
        return None, None, None
