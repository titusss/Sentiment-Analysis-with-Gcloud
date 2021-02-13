# Sentiment-Analysis-with-Gcloud
Simple fork of Gclouds NLP API tutorial for Sentiment Analysis. Exports a CSV with score, magnitude, and overall sentiment.

Made for the 'PodPlot' assignment for UC Berkeley's 'Technology Design Foundations'.

Follow this tutorial for authentification: https://cloud.google.com/natural-language/docs/sentiment-tutorial?authuser=2

Make sure that you have satisfied the prerequisites mentioned above and that the GOOGLE_APPLICATION_CREDENTIALS variable shows the path to your JSON credentials.

## Usage
Example with the 'The next outbreak? We’re not ready | Bill Gates' TED talk
```python
python3 sentimentAnalysis.py transcripts/TheNextOutbreak.txt
```
