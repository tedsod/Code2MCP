import os
import sys

# Path settings
source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source")
sys.path.insert(0, source_path)

# Necessary imports
from fastmcp import FastMCP
from src.textblob import blob, classifiers, decorators, formats, inflect, np_extractors, parsers, sentiments, taggers, tokenizers, utils

# Initialize FastMCP service
mcp = FastMCP("textblob_service")

@mcp.tool(name="analyze_blob", description="Analyze text using TextBlob.")
def analyze_blob(text: str) -> dict:
    """
    Analyze text using TextBlob.

    Parameters:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        blob_instance = blob.TextBlob(text)
        result = {
            "sentences": [str(sentence) for sentence in blob_instance.sentences],
            "words": list(blob_instance.words),
            "tags": blob_instance.tags,
            "noun_phrases": list(blob_instance.noun_phrases),
            "sentiment": blob_instance.sentiment._asdict()
        }
        return {"success": True, "result": result, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="classify_text", description="Classify text using a trained classifier.")
def classify_text(text: str, model_path: str) -> dict:
    """
    Classify text using a trained classifier.

    Parameters:
        text (str): The input text to classify.
        model_path (str): Path to the trained classifier model.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        classifier = classifiers.NaiveBayesClassifier.load(model_path)
        classification = classifier.classify(text)
        return {"success": True, "result": {"classification": classification}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="extract_noun_phrases", description="Extract noun phrases from text.")
def extract_noun_phrases(text: str) -> dict:
    """
    Extract noun phrases from text.

    Parameters:
        text (str): The input text to extract noun phrases from.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        blob_instance = blob.TextBlob(text)
        noun_phrases = list(blob_instance.noun_phrases)
        return {"success": True, "result": {"noun_phrases": noun_phrases}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="correct_spelling", description="Correct spelling in the given text.")
def correct_spelling(text: str) -> dict:
    """
    Correct spelling in the given text.

    Parameters:
        text (str): The input text to correct spelling.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        blob_instance = blob.TextBlob(text)
        corrected_text = str(blob_instance.correct())
        return {"success": True, "result": {"corrected_text": corrected_text}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="tokenize_text", description="Tokenize text into words and sentences.")
def tokenize_text(text: str) -> dict:
    """
    Tokenize text into words and sentences.

    Parameters:
        text (str): The input text to tokenize.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        tokenizer = tokenizers.WordTokenizer()
        word_tokens = tokenizer.tokenize(text)
        sentence_tokens = tokenizers.SentenceTokenizer().tokenize(text)
        return {"success": True, "result": {"words": word_tokens, "sentences": sentence_tokens}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="analyze_sentiment", description="Perform sentiment analysis on text.")
def analyze_sentiment(text: str) -> dict:
    """
    Perform sentiment analysis on text.

    Parameters:
        text (str): The input text to analyze sentiment.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        sentiment_analyzer = sentiments.PatternAnalyzer()
        sentiment = sentiment_analyzer.analyze(text)._asdict()
        return {"success": True, "result": {"sentiment": sentiment}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="parse_text", description="Parse text into syntax trees.")
def parse_text(text: str) -> dict:
    """
    Parse text into syntax trees.

    Parameters:
        text (str): The input text to parse.

    Returns:
        dict: A dictionary containing success, result, or error fields.
    """
    try:
        parser = parsers.PatternParser()
        parsed_result = parser.parse(text)
        return {"success": True, "result": {"parsed_text": parsed_result}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

def create_app() -> FastMCP:
    """
    Create and return the FastMCP application instance.

    Returns:
        FastMCP: The initialized FastMCP instance.
    """
    return mcp