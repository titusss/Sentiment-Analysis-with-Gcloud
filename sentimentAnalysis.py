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

from pytube import YouTube

def print_result(annotations, video_title, filename):
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
    print('Sentiment analysis finished. Here is your dataframe: ')
    print(df)
    df.to_csv('sentiment_' + filename + '.csv')
    print('The sentiment analysis results have been saved as: ' + 'sentiment_' + filename + '.csv')
    return 0

def analyze(subtitles, video_title, filename):
    """Run a sentiment analysis request on text within a passed filename."""
    print('Starting sentiment analysis on Gcloud Natural Language API')
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(content=subtitles, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    # Print the results
    print_result(annotations, video_title, filename)

def downloadSubtitles(youtube_url):
    """Download YouTube subtitles."""
    try:
        print('Downloading subtitles for: ' + youtube_url)
        source = YouTube(youtube_url)
        try:
            en_caption = source.captions["en"]
        except KeyError:
            en_caption = source.captions["a.en"]
        print("Succesfully downloaded subtitles for YouTube video: '" + source.title + "'")
        video_title = source.title.replace(" ", "_")
        caption = cleanCaption(en_caption.generate_srt_captions())
        filename = video_title + '_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        text_file = open("transcript_" + filename + '.txt', "w")
        text_file.write(caption)
        text_file.close()
        print("The transcript file has been successfully saved as: transcript_" + filename + '.txt')
        return caption, video_title, filename
    except:
        import sys
        sys.exit("The entered YouTube URL seems to be invalid. Make sure that you used quotation marks and that english subtitles are present. Example: python3 sentimentAnalysis.py 'https://www.youtube.com/watch?v=arj7oStGLkU'")

def cleanCaption(caption):
    caption_lines = caption.splitlines()
    cleaned_caption_list = caption_lines[2::4]
    caption_paragraph = ""
    for line in cleaned_caption_list:
        caption_paragraph += ' ' + line
    return caption_paragraph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "youtube_url",
        help="The URL in quotation marks to a YouTube video with english subtitles. Example: 'https://www.youtube.com/watch?v=arj7oStGLkU'",
    )
    args = parser.parse_args()
    subtitles, video_title, filename = downloadSubtitles(args.youtube_url)
    analyze(subtitles, video_title, filename)