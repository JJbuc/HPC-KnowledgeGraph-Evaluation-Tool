# HPC Knowledge Graph Evaluation Tool

## Overview
This project provides tools for evaluating Large Language Model (LLM) outputs against ground truth knowledge graphs in the High-Performance Computing (HPC) domain. It focuses on comparing generated triplets with expected outputs using advanced semantic similarity metrics.

## Features
- 🔍 Multiple parsing methods for different input formats
- 💡 Advanced sentence embedding models for semantic comparison
- 📊 Comprehensive evaluation metrics
- 🚀 Support for different similarity thresholds
- 📝 Detailed output analysis

## Project Structure
```
src/
├── parsers/               # Input parsing modules
│   ├── json_parser.py     # JSON file parsing
│   ├── text_parser.py     # Text file parsing
│   └── triplet_parser.py  # Triplet extraction
├── models/                # Core model implementations
│   ├── sentence_embeddings.py
│   └── similarity.py
├── utils/                 # Utility functions
│   ├── text_processing.py
│   └── data_utils.py
├── evaluation/            # Evaluation metrics
│   └── metrics.py
├── config.py             # Configuration settings
└── main.py               # Main execution script
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/hpc-kg-evaluation.git
cd hpc-kg-evaluation
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
Run the main evaluation script:
```bash
python src/main.py
```

### Configuration
Modify `config.py` to adjust:
- Model selection
- Similarity thresholds
- File paths
- Processing settings

### Input Formats
The tool supports multiple input formats:

1. JSON Format:
```json
{
    "id": "example",
    "triples": [
        {
            "sub": "entity1",
            "rel": "relation",
            "obj": "entity2"
        }
    ]
}
```

2. Text Format:
```text
entity1,relation,entity2
```

## Models

### Available Embedding Models
1. MiniLM-L6-v2 (Default)
   - Lightweight and fast
   - Good balance of performance and speed

2. MPNet-base-v2
   - Higher accuracy
   - More resource intensive

### Similarity Metrics
- Cosine similarity between embeddings
- Weighted component similarity for triplets
- Configurable thresholds

## Evaluation

### Metrics
The tool provides several evaluation metrics:
- Match count above threshold
- Average similarity scores
- Detailed mapping analysis

### Output Example
```
Results for threshold 0.75:
Average accuracy: 0.823
Number of matches: 145
```
