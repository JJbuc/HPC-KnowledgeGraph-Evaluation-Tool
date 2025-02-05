# src/main.py

from parsers.json_parser import extract_triples_by_id
from parsers.text_parser import latest_parser
from evaluation.metrics import evaluate_predictions
from statistics import mean

def main():
    # File paths
    ground_truth_path = 'GroundTruth/UpdatedDatasetJSON.json'
    predictions_path = 'newtriplets.txt'

    # Load data
    ground_truth = extract_triples_by_id(ground_truth_path)
    predicted = latest_parser(predictions_path)

    # Evaluate for different thresholds
    thresholds = [0.1, 0.75, 0.8]
    
    for threshold in thresholds:
        mappings, count = evaluate_predictions(
            ground_truth, 
            predicted, 
            threshold=threshold, 
            verbose=True
        )
        
        scores = list(mappings.values())
        avg_score = mean(scores) if scores else 0
        
        print(f'Results for threshold {threshold}:')
        print(f'Average accuracy: {avg_score:.3f}')
        print(f'Number of matches: {count}')
        print('---')

if __name__ == "__main__":
    main()
