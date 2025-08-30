import os
import sys

source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source")
sys.path.insert(0, source_path)

from fastmcp import FastMCP
from src.textblob import TextBlob, Word, Sentence, Blobber

mcp = FastMCP("textblob_service")

@mcp.tool(name="analyze_sentiment", description="Analyze the sentiment of a given text.")
def analyze_sentiment(text):
    """
    Analyze the sentiment of the provided text using TextBlob.

    Parameters:
    text (str): The text to analyze.

    Returns:
    dict: A dictionary containing success, result, and error fields.
    """
    try:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return {"success": True, "result": {"polarity": sentiment.polarity, "subjectivity": sentiment.subjectivity}, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="extract_noun_phrases", description="Extract noun phrases from a given text.")
def extract_noun_phrases(text):
    """
    Extract noun phrases from the provided text using TextBlob.

    Parameters:
    text (str): The text to extract noun phrases from.

    Returns:
    dict: A dictionary containing success, result, and error fields.
    """
    try:
        blob = TextBlob(text)
        noun_phrases = blob.noun_phrases
        return {"success": True, "result": noun_phrases, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="tag_parts_of_speech", description="Tag parts of speech in a given text.")
def tag_parts_of_speech(text):
    """
    Tag parts of speech in the provided text using TextBlob.

    Parameters:
    text (str): The text to tag parts of speech.

    Returns:
    dict: A dictionary containing success, result, and error fields.
    """
    try:
        blob = TextBlob(text)
        pos_tags = blob.tags
        return {"success": True, "result": pos_tags, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="pluralize_word", description="Pluralize a given word.")
def pluralize_word(word):
    """
    Pluralize the provided word using TextBlob's Word class.

    Parameters:
    word (str): The word to pluralize.

    Returns:
    dict: A dictionary containing success, result, and error fields.
    """
    try:
        word_obj = Word(word)
        plural_word = word_obj.pluralize()
        return {"success": True, "result": plural_word, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="health_check", description="Check the health of the service.")
def health_check():
    """
    Perform a health check of the service.

    Returns:
    dict: A dictionary containing success, result, and error fields.
    """
    try:
        return {"success": True, "result": "Service is healthy", "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="version_info", description="Get the version information of the service.")
def version_info():
    """
    Get the version information of the service.

    Returns:
    dict: A dictionary containing success, result, and error fields.
    """
    try:
        version = "1.0.0"
        return {"success": True, "result": version, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

def create_app():
    """
    Create and return the FastMCP application instance.

    Returns:
    FastMCP: The FastMCP application instance.
    """
    return mcp