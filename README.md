# Sentiment Analysis of YouTube videos with Gcloud NLP API
Automatically download and analyze any YouTube video subtitles based on sentiment with Google's Natural Language API.
Exports a CSV with score, magnitude, and overall sentiment and a transcript .txt file. Sentence query system is a simple fork of Gclouds NLP API tutorial for Sentiment Analysis. 

Made for the 'PodPlot' assignment for UC Berkeley's 'Technology Design Foundations'.

Follow this tutorial for authentification: https://cloud.google.com/natural-language/docs/sentiment-tutorial?authuser=2

Make sure that you have satisfied the prerequisites mentioned in the tutorial above and that the GOOGLE_APPLICATION_CREDENTIALS variable shows the path to your JSON credentials.

## Usage
```python
python3 sentimentAnalysis.py "YouTube URL"
```
Example with the 'The next outbreak? We’re not ready | Bill Gates' TED talk
```python
python3 sentimentAnalysis.py "https://www.youtube.com/watch?v=6Af6b_wyiwI"
```

## Installation
Clone this repository, cd into it, and install the required packages with pip.
```bash
git clone https://github.com/titusss/Sentiment-Analysis-with-Gcloud.git
cd Sentiment-Analysis-with-Gcloud
pip install -r requirements.txt
```

## Case Study
Example infographic created with Google Spreadsheet Charts.
![TDF_PodPlot_Export_03_MIRO](https://user-images.githubusercontent.com/26855197/107870085-7b49c700-6e4a-11eb-9e02-8f6397109019.png)
