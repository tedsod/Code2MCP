import os
import sys

# Set path
source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source")
sys.path.insert(0, source_path)

# Import modules from the TextBlob library
try:
    from src.textblob import TextBlob, Word, WordList, Sentence, Blobber
    from src.textblob import classifiers, decorators, download_corpora, exceptions, formats, inflect, mixins, np_extractors, parsers, sentiments, taggers, tokenizers, utils, wordnet
    import nltk
    import pattern
except ImportError as e:
    print(f"Import failed: {e}. Entering fallback mode.")

class Adapter:
    """
    MCP Import mode adapter class for handling TextBlob library functionality.
    """

    def __init__(self):
        self.mode = "import"
        self.blobber = None

    # -------------------- TextBlob Functionality Module --------------------

    def create_textblob(self, text):
        """
        Create a TextBlob instance.

        Parameters:
            text (str): The text to process.

        Returns:
            dict: A dictionary containing the status and the TextBlob instance or an error message.
        """
        try:
            blob = TextBlob(text)
            return {"status": "success", "blob": blob}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create TextBlob instance: {e}"}

    def analyze_sentiment(self, blob):
        """
        Analyze the sentiment of the text.

        Parameters:
            blob (TextBlob): The TextBlob instance.

        Returns:
            dict: A dictionary containing the status and the sentiment analysis result or an error message.
        """
        try:
            sentiment = blob.sentiment
            return {"status": "success", "sentiment": sentiment}
        except Exception as e:
            return {"status": "error", "message": f"Failed to analyze sentiment: {e}"}

    # -------------------- Word Functionality Module --------------------

    def create_word(self, text):
        """
        Create a Word instance.

        Parameters:
            text (str): The word text.

        Returns:
            dict: A dictionary containing the status and the Word instance or an error message.
        """
        try:
            word = Word(text)
            return {"status": "success", "word": word}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create Word instance: {e}"}

    def pluralize_word(self, word):
        """
        Pluralize a word.

        Parameters:
            word (Word): The Word instance.

        Returns:
            dict: A dictionary containing the status and the plural form or an error message.
        """
        try:
            plural = word.pluralize()
            return {"status": "success", "plural": plural}
        except Exception as e:
            return {"status": "error", "message": f"Failed to pluralize word: {e}"}

    # -------------------- Sentence Functionality Module --------------------

    def create_sentence(self, text):
        """
        Create a Sentence instance.

        Parameters:
            text (str): The sentence text.

        Returns:
            dict: A dictionary containing the status and the Sentence instance or an error message.
        """
        try:
            sentence = Sentence(text)
            return {"status": "success", "sentence": sentence}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create Sentence instance: {e}"}

    # -------------------- Blobber Functionality Module --------------------

    def create_blobber(self):
        """
        Create a Blobber instance.

        Returns:
            dict: A dictionary containing the status and the Blobber instance or an error message.
        """
        try:
            self.blobber = Blobber()
            return {"status": "success", "blobber": self.blobber}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create Blobber instance: {e}"}

    def process_text_with_blobber(self, text):
        """
        Process text using the Blobber.

        Parameters:
            text (str): The text to process.

        Returns:
            dict: A dictionary containing the status and the processing result or an error message.
        """
        if not self.blobber:
            return {"status": "error", "message": "Blobber instance not created"}
        try:
            blob = self.blobber(text)
            return {"status": "success", "blob": blob}
        except Exception as e:
            return {"status": "error", "message": f"Failed to process text with Blobber: {e}"}

    # -------------------- Fallback Mode Handling --------------------

    def downgrade_mode(self):
        """
        Handle the fallback mode for import failures.

        Returns:
            dict: A dictionary containing the status and fallback information.
        """
        return {"status": "warning", "message": "Entered fallback mode, some functionality may be unavailable"}

# Instantiate the adapter
adapter = Adapter()