import numpy as np

def create_embedding_matrix(corpus, embedding_dim):
    # Preprocessing
    vocabulary = {}
    index = 0
    
    # Build the vocabulary from the corpus
    for sentence in corpus:
        words = sentence.lower().split()
        for word in words:
            if word not in vocabulary:
                vocabulary[word] = index
                index += 1

    # Vocabulary size
    V = len(vocabulary)

    # Initialize embedding matrix with random values between 0 and 1
    E = np.random.rand(V, embedding_dim)

    # Define get_word_vector function
    def get_word_vector(word):
        word = word.lower()
        if word in vocabulary:
            idx = vocabulary[word]
            return E[idx]
        else:
            return np.zeros(embedding_dim)

    return E, vocabulary, get_word_vector

# Example usage
corpus = [
    "I love machine learning",
    "Machine learning is amazing",
    "I love learning new things"
]
embedding_dim = 3

# Create the embedding matrix and related objects
E, vocabulary, get_word_vector = create_embedding_matrix(corpus, embedding_dim)

# Print the vocabulary and embedding matrix
print("Vocabulary:", vocabulary)
print("Embedding Matrix E:\n", E)

# Test get_word_vector with a known word
word = "learning"
vector = get_word_vector(word)
print(f"Embedding for '{word}':", vector)

# Test get_word_vector with an unknown word
word = "unknown"
vector = get_word_vector(word)
print(f"Embedding for '{word}':", vector)
