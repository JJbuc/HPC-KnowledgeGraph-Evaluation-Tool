# src/models/similarity.py

from typing import Dict, List, Tuple
import torch
from sentence_transformers import util

def compute_cosine_similarity(embeddings1: torch.Tensor,
                            embeddings2: torch.Tensor) -> torch.Tensor:
    """Compute cosine similarity between two sets of embeddings."""
    return util.pytorch_cos_sim(embeddings1, embeddings2)

def create_similarity_matrix(dict1: Dict[str, torch.Tensor],
                           dict2: Dict[str, torch.Tensor]) -> Dict[str, float]:
    """Create a similarity matrix between two dictionaries of embeddings."""
    similarity_dict = {}
    for key1, emb1 in dict1.items():
        for key2, emb2 in dict2.items():
            similarity = util.pytorch_cos_sim(emb1, emb2)
            compare_key = f"{key1}-{key2}"
            similarity_dict[compare_key] = similarity.item()
    return similarity_dict

def find_best_match(query: str,
                    candidates: List[str],
                    similarity_dict: Dict[str, float],
                    threshold: float = 0.6) -> Tuple[float, int, str]:
    """Find the best matching candidate for a query string."""
    scores = []
    for candidate in candidates:
        similarity_key = f"{query}-{candidate}"
        score = similarity_dict.get(similarity_key, 0)
        scores.append(score)
    
    max_score = max(scores)
    best_idx = scores.index(max_score)
    
    if max_score > threshold:
        mapping = f"{query}-->{candidates[best_idx]}"
        return max_score, best_idx, mapping
    else:
        mapping = f"{query}-->{candidates[best_idx]}"
        return -1, best_idx, mapping

def compute_weighted_similarity(subject_sim: float,
                              relation_sim: float,
                              object_sim: float,
                              weights: Tuple[float, float, float] = (0.33, 0.34, 0.33)) -> float:
    """Compute weighted similarity score for triplet components."""
    return (weights[0] * subject_sim +
            weights[1] * relation_sim +
            weights[2] * object_sim)
