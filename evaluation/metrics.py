# src/evaluation/metrics.py

from models.sentence_embeddings import EmbeddingModel
from utils.data_utils import get_unique_elements

def create_similarity_dict(ground_truth, predicted, embedding_model):
    """Create similarity dictionary between ground truth and predicted triplets."""
    dict1 = embedding_model.create_embeddings_dict(ground_truth)
    dict2 = embedding_model.create_embeddings_dict(predicted)
    return embedding_model.compute_similarity(dict1, dict2)

def map_triplet(triplet, triplet_list, similarity_dict, threshold=0.6):
    """Map a single triplet to the most similar one in the list."""
    final_scores = []
    for candidate in triplet_list:
        similarity_key = f"{triplet}-{candidate}"
        score = similarity_dict.get(similarity_key, 0)
        final_scores.append(score)

    max_score = max(final_scores)
    if max_score > threshold:
        idx = final_scores.index(max_score)
        mapping = f"{triplet}-->{triplet_list[idx]}"
        return final_scores, max_score, idx, mapping
    else:
        idx = final_scores.index(max_score)
        mapping = f"{triplet}-->{triplet_list[idx]}"
        return final_scores, -1, idx, mapping

def evaluate_predictions(ground_truth, predicted, threshold=0.75, verbose=False):
    """Evaluate predictions against ground truth."""
    if verbose:
        print(f"Evaluating {len(ground_truth)} ground truth triplets")

    embedding_model = EmbeddingModel()
    similarity_dict = create_similarity_dict(ground_truth, predicted, embedding_model)
    
    mappings = {}
    count = 0
    
    for triplet in ground_truth:
        _, max_score, idx, mapping = map_triplet(triplet, predicted, similarity_dict, threshold)
        if max_score > 0:
            count += 1
            mappings[mapping] = max_score
            
    if verbose:
        print(f"Found {count} matches above threshold {threshold}")
        
    return mappings, count
