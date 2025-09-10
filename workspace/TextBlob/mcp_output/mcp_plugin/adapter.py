import os
import sys

# Path settings
source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source")
sys.path.insert(0, source_path)

# Import statements
try:
    from src.textblob import TextBlob, Blobber, Word, WordList, Sentence
    from src.textblob.tokenizers import WordTokenizer, SentenceTokenizer
    from src.textblob.taggers import NLTKTagger, PatternTagger
    from src.textblob.np_extractors import FastNPExtractor, ConllExtractor
    from src.textblob.sentiments import PatternAnalyzer, NaiveBayesAnalyzer
    from src.textblob.parsers import PatternParser
    from src.textblob.classifiers import NaiveBayesClassifier, DecisionTreeClassifier, MaxEntClassifier
except ImportError as e:
    print("Error importing modules: ", str(e))
    print("Fallback mode activated. Ensure the source directory is correctly set.")
    fallback_mode = True
else:
    fallback_mode = False

# Adapter class
class Adapter:
    """
    Adapter class for MCP plugin integration with TextBlob library.
    Provides methods to utilize TextBlob's core classes and functions.
    """
    def __init__(self):
        self.mode = "import" if not fallback_mode else "fallback"

    # -------------------- Core Class Methods --------------------

    def create_textblob(self, text):
        """
        Create an instance of TextBlob.
        
        Parameters:
            text (str): The text to process.
        
        Returns:
            dict: Status and TextBlob instance or error message.
        """
        try:
            blob = TextBlob(text)
            return {"status": "success", "data": blob}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create TextBlob instance: {str(e)}"}

    def create_blobber(self, tokenizer=None, np_extractor=None):
        """
        Create an instance of Blobber with optional custom components.
        
        Parameters:
            tokenizer (object): Custom tokenizer instance.
            np_extractor (object): Custom noun phrase extractor instance.
        
        Returns:
            dict: Status and Blobber instance or error message.
        """
        try:
            blobber = Blobber(tokenizer=tokenizer, np_extractor=np_extractor)
            return {"status": "success", "data": blobber}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create Blobber instance: {str(e)}"}

    def create_word(self, word):
        """
        Create an instance of Word.
        
        Parameters:
            word (str): The word to process.
        
        Returns:
            dict: Status and Word instance or error message.
        """
        try:
            word_instance = Word(word)
            return {"status": "success", "data": word_instance}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create Word instance: {str(e)}"}

    def create_wordlist(self, words):
        """
        Create an instance of WordList.
        
        Parameters:
            words (list): List of words to process.
        
        Returns:
            dict: Status and WordList instance or error message.
        """
        try:
            wordlist_instance = WordList(words)
            return {"status": "success", "data": wordlist_instance}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create WordList instance: {str(e)}"}

    def create_sentence(self, text, start_index=0, end_index=None):
        """
        Create an instance of Sentence.
        
        Parameters:
            text (str): The sentence text.
            start_index (int): Start index of the sentence.
            end_index (int): End index of the sentence.
        
        Returns:
            dict: Status and Sentence instance or error message.
        """
        try:
            sentence_instance = Sentence(text, start_index=start_index, end_index=end_index)
            return {"status": "success", "data": sentence_instance}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create Sentence instance: {str(e)}"}

    # -------------------- NLP Component Methods --------------------

    def tokenize_text(self, text, tokenizer_type="word"):
        """
        Tokenize text using the specified tokenizer type.
        
        Parameters:
            text (str): The text to tokenize.
            tokenizer_type (str): Type of tokenizer ("word" or "sentence").
        
        Returns:
            dict: Status and tokenized text or error message.
        """
        try:
            tokenizer = WordTokenizer() if tokenizer_type == "word" else SentenceTokenizer()
            tokens = tokenizer.tokenize(text)
            return {"status": "success", "data": tokens}
        except Exception as e:
            return {"status": "error", "message": f"Failed to tokenize text: {str(e)}"}

    def tag_pos(self, text, tagger_type="nltk"):
        """
        Perform part-of-speech tagging on text using the specified tagger type.
        
        Parameters:
            text (str): The text to tag.
            tagger_type (str): Type of tagger ("nltk" or "pattern").
        
        Returns:
            dict: Status and POS tags or error message.
        """
        try:
            tagger = NLTKTagger() if tagger_type == "nltk" else PatternTagger()
            tags = tagger.tag(text)
            return {"status": "success", "data": tags}
        except Exception as e:
            return {"status": "error", "message": f"Failed to perform POS tagging: {str(e)}"}

    def extract_noun_phrases(self, text, extractor_type="fast"):
        """
        Extract noun phrases from text using the specified extractor type.
        
        Parameters:
            text (str): The text to process.
            extractor_type (str): Type of extractor ("fast" or "conll").
        
        Returns:
            dict: Status and noun phrases or error message.
        """
        try:
            extractor = FastNPExtractor() if extractor_type == "fast" else ConllExtractor()
            noun_phrases = extractor.extract(text)
            return {"status": "success", "data": noun_phrases}
        except Exception as e:
            return {"status": "error", "message": f"Failed to extract noun phrases: {str(e)}"}

    def analyze_sentiment(self, text, analyzer_type="pattern"):
        """
        Analyze sentiment of text using the specified analyzer type.
        
        Parameters:
            text (str): The text to analyze.
            analyzer_type (str): Type of analyzer ("pattern" or "naivebayes").
        
        Returns:
            dict: Status and sentiment analysis result or error message.
        """
        try:
            analyzer = PatternAnalyzer() if analyzer_type == "pattern" else NaiveBayesAnalyzer()
            sentiment = analyzer.analyze(text)
            return {"status": "success", "data": sentiment}
        except Exception as e:
            return {"status": "error", "message": f"Failed to analyze sentiment: {str(e)}"}

    def parse_text(self, text):
        """
        Parse text to generate syntax trees.
        
        Parameters:
            text (str): The text to parse.
        
        Returns:
            dict: Status and parsed result or error message.
        """
        try:
            parser = PatternParser()
            parsed_result = parser.parse(text)
            return {"status": "success", "data": parsed_result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to parse text: {str(e)}"}

    def classify_text(self, text, classifier_type="naivebayes", training_data=None):
        """
        Classify text using the specified classifier type.
        
        Parameters:
            text (str): The text to classify.
            classifier_type (str): Type of classifier ("naivebayes", "decisiontree", "maxent").
            training_data (list): Training data for the classifier.
        
        Returns:
            dict: Status and classification result or error message.
        """
        try:
            if classifier_type == "naivebayes":
                classifier = NaiveBayesClassifier(training_data)
            elif classifier_type == "decisiontree":
                classifier = DecisionTreeClassifier(training_data)
            elif classifier_type == "maxent":
                classifier = MaxEntClassifier(training_data)
            else:
                raise ValueError("Invalid classifier type specified.")
            classification = classifier.classify(text)
            return {"status": "success", "data": classification}
        except Exception as e:
            return {"status": "error", "message": f"Failed to classify text: {str(e)}"}

    # -------------------- Utility Methods --------------------

    def check_mode(self):
        """
        Check the current mode of the adapter.
        
        Returns:
            dict: Status and current mode.
        """
        return {"status": "success", "data": self.mode}