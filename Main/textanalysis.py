import nltk  # Importing the Natural Language Toolkit (NLTK) library for text processing
from nltk.corpus import cmudict  # Importing CMU Pronouncing Dictionary for syllable counting

# Run these commands once to download required datasets
# nltk.download('cmudict')  # Download CMU Pronouncing Dictionary
# nltk.download('punkt')  # Download the Punkt tokenizer models

# File paths for stopwords and sentiment words
stopwords_file_path = 'application/StopWords_ALL.txt'
positive_words_file_path = 'MasterDictionary/positive-words.txt'
negative_words_file_path = 'MasterDictionary/negative-words.txt'
treshold = 2  # Syllable threshold to classify a word as complex
pronoun_list = ["I", "we", "my", "ours", "us", "We", "My", "Ours", "Us"]  # List of pronouns to check for personal pronouns
d = cmudict.dict()  # CMU Pronouncing Dictionary for syllable counting

# Function to remove stopwords from the text
def remove_stopwords(text):
    # Open and read the stopwords file
    with open(stopwords_file_path, 'r', encoding='utf-8') as file:
        stopwords = {line.strip().lower() for line in file}
    
    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)
    
    # Filter out stopwords from the tokens
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
    
    return filtered_tokens

# Function to calculate the positive and negative sentiment scores
def calculate_postive_negative_score(tokens):
    positive_score = 0
    negative_score = 0

    # Open and read the positive words file
    with open(positive_words_file_path, 'r', encoding='utf-8') as p:
        postive_words = {line.strip().lower() for line in p}

    # Open and read the negative words file
    with open(negative_words_file_path, 'r', encoding='utf-8', errors='replace') as n:
        negative_words = {line.strip().lower() for line in n}

    # Count occurrences of positive and negative words in the tokens
    for word in tokens:
        if word.lower() in postive_words:
            positive_score += 1
        if word.lower() in negative_words:
            negative_score += 1    

    return positive_score, negative_score

# Function to calculate polarity and subjectivity based on sentiment scores
def calculate_polarity_and_subjectivity(positive_score, negative_score, word_count):
    # Polarity measures the sentiment: positive or negative
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    
    # Subjectivity measures how subjective or objective the text is
    subjectivity_score = (positive_score + negative_score) / ((word_count) + 0.000001)
    
    return polarity_score, subjectivity_score

# Function to count syllables in a word
def count_syllabe(word):
    # Use CMU Pronouncing Dictionary to find syllable count
    if word.lower() in d:
        return max([len([s for s in pron if s[-1].isdigit()]) for pron in d[word.lower()]])
    else:
        return 0  # If word not in dictionary, return 0 syllables
    
syllable_list = []  # List to store syllable counts

# Function to calculate complex words and average syllable count
def complex_word_count(tokens):
    # Complex words are those with syllable count greater than or equal to threshold
    complex_words = [word for word in tokens if count_syllabe(word) >= treshold]
    
    # Calculate average syllable count across all tokens
    for word in tokens:
        syllable_list.append(count_syllabe(word))
    avg_syllable = sum(syllable_list) / len(syllable_list)

    return len(complex_words), avg_syllable

# Function to perform readability analysis on the text
def readabilty_analysis(text, word_count):
    # Tokenize text into sentences and words
    sentences = nltk.tokenize.sent_tokenize(text)
    tokens = nltk.word_tokenize(text)
    
    # Calculate the number of sentences and words per sentence
    no_of_sentences = len(sentences)
    words_in_sentences = [len(sentence.split()) for sentence in sentences]
    
    # Calculate average words per sentence
    if len(sentences) > 0:
        avg_words_per_sentence = sum(words_in_sentences) / len(sentences)
    
    # Calculate average sentence length
    no_of_tokens = len(tokens)
    average_sentence_length = no_of_tokens / no_of_sentences

    # Calculate complex words count and average syllables per word
    complex_words_count, avg_syllable = complex_word_count(tokens)
    
    # Calculate percentage of complex words in the text
    complex_word_percent = complex_words_count / word_count
    
    # Calculate FOG Index (used for readability)
    fog_index = 0.4 * (average_sentence_length + complex_word_percent)
    
    return average_sentence_length, complex_word_percent, fog_index, avg_syllable, avg_words_per_sentence, complex_words_count

# Function to detect personal pronouns in the text
def personal_pronoun_in_text(text):
    tokens = nltk.word_tokenize(text)
    # Create a list to store found pronouns
    pronouns = []
    
    # Check if any word in the tokens is a personal pronoun
    for word in tokens:
        if word in pronoun_list:
            if word not in pronouns:
                pronouns.append(word)
    
    # Return found pronouns or "none" if no pronouns are found
    if not pronouns:
        return "none"
    else:
        return " ".join(pronouns)
