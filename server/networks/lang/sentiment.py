import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the trained model with the custom object scope
custom_objects = {"not_equal": tf.math.not_equal}
with tf.keras.utils.custom_object_scope(custom_objects):
    model = load_model("seq2seq_phrase_boundary_detection_model.keras")

# Tokenize the input sentence
tokenizer = Tokenizer()
tokenizer.fit_on_texts([""])
input_sentence = "Hi Im steve and I love cheese! Every so often I go to halifax."
input_sequence = tokenizer.texts_to_sequences([input_sentence])

# Pad the tokenized sequence
max_sequence_length = 50
input_sequence_padded = pad_sequences(
    input_sequence, maxlen=max_sequence_length, padding="post"
)

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
