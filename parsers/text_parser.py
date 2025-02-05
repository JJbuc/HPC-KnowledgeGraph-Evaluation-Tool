# src/parsers/text_parser.py

def latest_parser(file_path):
    """Parse the latest format of triplets from text file."""
    formatted_output = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.lower()
            sub, rel, obj = line.split(',')
            sub = sub.replace('_', ' ').strip()
            rel = rel.replace('_', ' ').strip()
            obj = obj.replace('_', ' ').replace('\n', '').strip()
            formatted_output.append(f"{sub} {rel} {obj}")
    return formatted_output

def extract_triplets_from_text(txt_file_path):
    """Extract triplets from text file with specific format."""
    formatted_output = []
    try:
        with open(txt_file_path, 'r') as file:
            for line in file:
                if line.strip():
                    input_dict = eval(line)
                    sub = clean_text(input_dict['sub'].strip(':'))
                    rel = clean_text(input_dict['rel'].strip(':'))
                    obj = clean_text(input_dict['obj'].strip(':'))
                    formatted_output.append(f"{sub} {rel} {obj}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return formatted_output

def clean_text(text):
    """Clean text by removing special characters and extra spaces."""
    text = text.replace('`', '').replace('_', ' ').replace('"', '').replace("'", '')
    return ' '.join(text.split())
