# src/models/sentence_embeddings.py

from sentence_transformers import SentenceTransformer, util

class EmbeddingModel:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def get_embeddings(self, sentences):
        """Get embeddings for a list of sentences."""
        return self.model.encode(sentences, convert_to_tensor=True)

    def create_embeddings_dict(self, unique_list):
        """Create a dictionary mapping text to embeddings."""
        embeddings = self.get_embeddings(unique_list)
        return {unique_list[i]: embeddings[i] 
                for i in range(min(len(unique_list), len(embeddings)))}

    def compute_similarity(self, dict1, dict2):
        """Compute cosine similarity between two dictionaries of embeddings."""
        similarity_dict = {}
        for key1, emb1 in dict1.items():
            for key2, emb2 in dict2.items():
                similarity = util.pytorch_cos_sim(emb1, emb2)
                compare_key = f"{key1}-{key2}"
                similarity_dict[compare_key] = similarity.item()
        return similarity_dict
