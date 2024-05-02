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


# Function to preprocess a proposition into numerical features
def preprocess_proposition(proposition):
    # Perform sentiment analysis using TextBlob
    sentiment_score_tb = TextBlob(proposition).sentiment.polarity
    print(f"TextBlob Sentiment score: {sentiment_score_tb}")

    # Placeholder for other attributes
    # You can add more logic here to extract additional attributes
    attributes = [
        "Financial Impact",
        "Social Impact",
        "Environmental Impact",
        "Political Impact",
        "Other",
    ]

    # Perform one-hot encoding for categorical attributes
    encoded_attributes = [
        int(
            any(
                attr_word in proposition.lower().split()
                for attr_word in attr.lower().split()
            )
        )
        for attr in attributes
    ]
    print("Encoded Attributes:", encoded_attributes)

    # Combine sentiment score and encoded attributes into a single input array
    input_data = np.array([[sentiment_score_tb] + encoded_attributes], dtype=np.float32)
    print("Input Data:", input_data)

    return input_data


# Function to gather user feedback (good idea or not)
def gather_user_feedback():
    feedback = input("Is this a good idea? (yes/no): ").lower()
    if feedback == "yes":
        return 1
    elif feedback == "no":
        return 0
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return gather_user_feedback()


# Main function to read the proposition, gather feedback, and update the neural network
def main():
    # Step 1: Define the problem
    # The government AI predicts whether implementing a proposition will benefit the institution.

    # Step 2: Design the neural network
    government_model = GovernmentNN()

    # Step 3: Gather training data
    # We don't need this step anymore since we'll gather feedback in real-time

    # Step 4: Load pre-trained model weights (if available)
    # government_model.load_weights("government_model_weights.h5")

    # Step 5: Simulate decision-making and learning loop
    while True:
        # Read the proposition from the command line
        proposition = input("Enter a proposition: ")

        # Preprocess the proposition into numerical features
        proposition_input = preprocess_proposition(proposition)

        # Gather user feedback
        feedback = gather_user_feedback()

        # Update the neural network based on the feedback
        government_model.compile(
            optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
        )
        print(proposition_input, feedback)
        government_model.fit(proposition_input, feedback, epochs=1, verbose=1)

        # Ask if the user wants to continue
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != "yes":
            break

    # Save the trained model weights
    # government_model.save_weights("government_model_weights.h5")


if __name__ == "__main__":
    main()
