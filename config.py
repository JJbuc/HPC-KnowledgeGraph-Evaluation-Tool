# src/config.py

class Config:
    # Model settings
    DEFAULT_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
    ALTERNATIVE_MODEL = 'sentence-transformers/all-mpnet-base-v2'
    
    # Similarity thresholds
    DEFAULT_THRESHOLD = 0.75
    EVALUATION_THRESHOLDS = [0.1, 0.75, 0.8]
    
    # Component weights for triplet similarity
    TRIPLET_WEIGHTS = {
        'subject': 0.33,
        'relation': 0.34,
        'object': 0.33
    }
    
    # File paths
    GROUND_TRUTH_PATH = 'GroundTruth/UpdatedDatasetJSON.json'
    PREDICTIONS_PATH = 'newtriplets.txt'
    OUTPUT_DIR = 'output'
    
    # Processing settings
    BATCH_SIZE = 32
    USE_CUDA = True
    
    # Logging settings
    VERBOSE = False
    LOG_FILE = 'evaluation.log'
