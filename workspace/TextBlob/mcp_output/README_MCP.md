# TextBlob MCP (Model Context Protocol) Service

## Project Introduction

TextBlob is a Python library designed for processing textual data. It provides a simple and intuitive API for common natural language processing (NLP) tasks, including sentiment analysis, noun phrase extraction, tokenization, part-of-speech tagging, and text classification. Built on top of robust libraries like NLTK and Pattern, TextBlob simplifies complex NLP operations for developers.

## Installation Method

To install TextBlob, ensure you have Python 3.9 or later installed. TextBlob requires the following dependencies:
- `nltk`
- `numpy`
- `pattern`  
Optional dependency:
- `scikit-learn` (for advanced classification tasks)

Install TextBlob using pip:
```
pip install textblob
```

Additionally, download the necessary NLTK corpora:
```
python -m textblob.download_corpora
```

## Quick Start

Here is a quick example to get started with TextBlob MCP (Model Context Protocol):

1. Create a `TextBlob` object:
```
from textblob import TextBlob

text = "TextBlob makes NLP simple and intuitive."
blob = TextBlob(text)
```

2. Perform common NLP tasks:
- Sentiment Analysis:
```
blob.sentiment
```
- Noun Phrase Extraction:
```
blob.noun_phrases
```
- Tokenization:
```
blob.words
blob.sentences
```
- Part-of-Speech Tagging:
```
blob.tags
```
- Text Classification:
```
from textblob.classifiers import NaiveBayesClassifier

train_data = [("I love this library!", "pos"), ("I hate bugs.", "neg")]
classifier = NaiveBayesClassifier(train_data)
classifier.classify("This is amazing!")
```

## Available Tools and Endpoints List

TextBlob MCP provides the following tools and services:

1. **TextBlob Class**  
   - Core service for text processing. Provides methods for sentiment analysis, noun phrase extraction, tokenization, and more.

2. **WordTokenizer and SentenceTokenizer**  
   - Services for splitting text into words and sentences.

3. **Part-of-Speech Tagging (PerceptronTagger)**  
   - Assigns grammatical parts of speech to words.

4. **Sentiment Analysis (PatternAnalyzer, NaiveBayesAnalyzer)**  
   - Calculates polarity (positive/negative) and subjectivity of text.

5. **Text Classification (NaiveBayesClassifier)**  
   - Categorizes text into predefined classes.

6. **Utility Services**  
   - Includes functions for text preprocessing, such as punctuation stripping and case normalization.

## Common Issues and Notes

- **Dependencies**: Ensure all required dependencies (`nltk`, `numpy`, `pattern`) are installed. Optional dependencies like `scikit-learn` may be needed for advanced classification tasks.
- **Environment**: TextBlob supports Python 3.9 and later. Compatibility with older versions is not guaranteed.
- **Performance**: While TextBlob is designed for simplicity, it may not be suitable for high-performance or large-scale NLP tasks. Consider using specialized libraries for such use cases.
- **Corpora**: Downloading NLTK corpora is mandatory for certain functionalities like tagging and sentiment analysis.

## Reference Links or Documentation

- [TextBlob GitHub Repository](https://github.com/sloria/TextBlob)
- [Official Documentation](https://textblob.readthedocs.io/en/dev/)
- [NLTK Documentation](https://www.nltk.org/)
- [Pattern Library](https://github.com/clips/pattern)

For further details, refer to the official documentation and explore advanced features like customization and extension services.