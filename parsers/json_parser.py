# src/parsers/json_parser.py

import json

def extract_triples_by_id(json_file_path):
    """Extract triples from JSON file."""
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    triples = []
    for item in data:
        triplets = item.get('triples', [])
        for triplet in triplets:
            rel = triplet['rel'].replace('_', ' ')
            sub = triplet['sub'].replace('_', ' ')
            obj = triplet['obj'].replace('_', ' ')
            triplet['rel'] = rel
            triplet['sub'] = sub
            triplet['obj'] = obj
        triples.extend(triplets)

    formatted_triples = [f"{triple['sub']} {triple['rel']} {triple['obj']}" 
                        for triple in triples]
    return formatted_triples

def extract_sentences_by_id(json_file_path):
    """Extract sentences from JSON file."""
    formatted = []
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        text = item.get('sent', '')
        sentences = text.split('.')
        formatted.extend(sentence.strip() for sentence in sentences if sentence.strip())

    return formatted
