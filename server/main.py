import numpy as np
import tensorflow as tf
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK's sentiment analyzer
nltk.download("vader_lexicon")
sid = SentimentIntensityAnalyzer()


# Define the neural network architecture
class GovernmentNN(tf.keras.Model):
    def __init__(self):
        super(GovernmentNN, self).__init__()
        self.dense1 = tf.keras.layers.Dense(
            6, activation="relu"
        )  # Adjusted to match the number of features
        self.dense2 = tf.keras.layers.Dense(32, activation="relu")
        self.dense3 = tf.keras.layers.Dense(1, activation="sigmoid")

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        return self.dense3(x)
