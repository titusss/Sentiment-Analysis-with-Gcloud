# Call NLP Gcloud API for Sentiment Analysis
# Follow this tutorial: https://cloud.google.com/natural-language/docs/sentiment-tutorial?authuser=2
# to setup your Gcloud project for NLP
#
# Set GOOGLE_APPLICATION_CREDENTIALS env var to the path of your JSON credentials
# This will output a CSV from a pandas dataframe
# Install Pandas with pip3 install pandas
# Query script is from Gclouds example tutorial

import argparse

import pandas as pd

from google.cloud import language_v1

from datetime import datetime


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    results = {}
    for index, sentence in enumerate(annotations.sentences):
        # print(sentence)
        sentence_sentiment = sentence.sentiment.score
        print(
            "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
        )
        results[index] = [sentence.text.content, sentence.sentiment.score, sentence.sentiment.magnitude, sentence_sentiment]

    df = pd.DataFrame.from_dict(results, orient='index', columns=['sentence', 'score', 'magnitude', 'overall sentiment'])
    print(
        "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    )
    print(df)
    df.to_csv('results_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.csv')
    print('The results have been saved as: ' + 'results_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.csv')
    return 0

def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    with open(movie_review_filename, "r") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()
    # Remove new lines
    content = content.replace('\n', ' ').replace('\r', '').replace('  ', ' ')
    document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    # Print the results
    print_result(annotations)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "movie_review_filename",
        help="The filename of the movie review you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.movie_review_filename)