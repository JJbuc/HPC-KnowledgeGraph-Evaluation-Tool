# src/models/__init__.py

from .sentence_embeddings import EmbeddingModel
from .similarity import (
    compute_cosine_similarity,
    create_similarity_matrix,
    find_best_match,
    compute_weighted_similarity
)

__all__ = [
    'EmbeddingModel',
    'compute_cosine_similarity',
    'create_similarity_matrix',
    'find_best_match',
    'compute_weighted_similarity'
]
