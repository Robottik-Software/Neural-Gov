import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Generate synthetic data
sentences = [
    "Hi Im steve and I love cheese!",
    "Every so often I go to halifax.",
    
]
phrase_boundaries = [
    [(0, 22), (23, 42)],  # Boundaries for the first sentence
    [(0, 26), (27, 45)]   # Boundaries for the second sentence
]

# Tokenize words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
vocab_size = len(tokenizer.word_index) + 1

# Convert sentences to sequences
sequences = tokenizer.texts_to_sequences(sentences)

# Pad sequences to ensure uniform length
max_sequence_length = max(len(seq) for seq in sequences)
sequences_padded = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# Create input and target data for the model
encoder_input_data = sequences_padded
decoder_target_data = np.zeros((len(sentences), max_sequence_length, 2), dtype="float32")

# Set target labels for phrase boundaries
for i, bounds in enumerate(phrase_boundaries):
    for bound in bounds:
        start, end = bound
        decoder_target_data[i, start:end, 1] = 1

# Define Seq2Seq model architecture
latent_dim = 256

# Encoder
encoder_inputs = Input(shape=(None,))
encoder_embedding = tf.keras.layers.Embedding(vocab_size, latent_dim, mask_zero=True)(encoder_inputs)
encoder_lstm = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
encoder_states = [state_h, state_c]

# Decoder
decoder_inputs = Input(shape=(None,))
decoder_embedding = tf.keras.layers.Embedding(vocab_size, latent_dim, mask_zero=True)(decoder_inputs)
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
decoder_dense = Dense(2, activation="softmax")
decoder_outputs = decoder_dense(decoder_outputs)

# Define the model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Train the model
model.fit(
    [encoder_input_data, sequences_padded],
    decoder_target_data,
    batch_size=1,
    epochs=100
)

# Save the model
model.save("seq2seq_phrase_boundary_detection_model.keras")

# Use the trained model for inference

# Load the trained model
model = tf.keras.models.load_model("seq2seq_phrase_boundary_detection_model.keras")

# Tokenize the input sentence
input_sentence = "Hi Im steve and I love cheese! Every so often I go to halifax."
input_sequence = tokenizer.texts_to_sequences([input_sentence])

# Pad the tokenized sequence
input_sequence_padded = pad_sequences(input_sequence, maxlen=max_sequence_length, padding='post')

# Predict phrase boundaries
predictions = model.predict([input_sequence_padded, input_sequence_padded])

# Interpret predictions
phrase_boundaries = []
for i, prediction in enumerate(predictions[0]):
    # Identify positions where the model predicts the start or end of a phrase
    if np.argmax(prediction) == 1:
        phrase_boundaries.append(i)

# Generate phrases based on boundaries
phrases = []
for i in range(len(phrase_boundaries) - 1):
    start_index = phrase_boundaries[i]
    end_index = phrase_boundaries[i + 1]
    phrases.append(input_sentence[start_index:end_index])

# Print the identified phrases
print("Input Sentence:", input_sentence)
print("Predicted Phrases:", phrases)
