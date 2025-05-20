import pandas as pd  # Importing pandas for data manipulation and file handling
import articleextraction as artx  # Importing articleextraction module (assumed to handle article fetching)
import textanalysis as ta  # Importing textanalysis module (assumed to handle text processing)

input_file_path ="Input.xlsx"  # Path to the input Excel file containing URLs and IDs

# Reading the input Excel file into a pandas DataFrame
df = pd.read_excel(input_file_path)

# Lists to store the data from the first two columns of the Excel file
column1 = []
column2 = []

# Iterating over each row of the DataFrame to extract the URL and its corresponding ID
for index, row in df.iterrows():
    column1.append(row.iloc[0])  # Append URL_ID from the first column
    column2.append(row.iloc[1])  # Append URL from the second column

# Creating an empty DataFrame for storing the analysis results
df1 = pd.DataFrame(columns=["URL_ID", "URL", "Positive_Score", "Negative_Score", "Polarity_Score", "Subjectivity_score", "AVG_Sentence_Length", "Percentage_Of_Complex_words", "FOG_index", "AVG_number_of_words_per_sentence", "complex_word_count", "word_count", "Syallble_per_word", "Personal_pronouns", "AVG_word_length"], dtype="object")

# Looping through the URLs and IDs to process each article
for id, link in zip(column1, column2):
    print(f"URL_ID: {id} URL: {link}")
    
    # Extracting article content using the articleextraction module
    article_content = artx.get_text_form_url(link)
    
    # Removing stopwords from the article content and tokenizing the text
    tokens = ta.remove_stopwords(article_content)
    
    # Counting the number of words in the article
    word_count = len(tokens)
    
    # Calculating the positive and negative sentiment scores
    positive_score, negative_score = ta.calculate_postive_negative_score(tokens)
    
    # Calculating the polarity and subjectivity of the article
    polarity_score, subjectivity_score = ta.calculate_polarity_and_subjectivity(positive_score, negative_score, word_count)
    
    # Performing readability analysis on the article
    avg_sl, per_of_Cmplx_words, fog_index, avg_syllable, avg_word_per_sent, cmplx_wrd_cnt = ta.readabilty_analysis(article_content, len(tokens))
    
    # Identifying personal pronouns in the article
    personal_pronouns = ta.personal_pronoun_in_text(article_content)
    
    # Calculating the average word length by summing the length of all words and dividing by word count
    total_word_length = sum(len(word) for word in tokens)
    avg_word_len = total_word_length / word_count
    
    # Creating a new row with the analysis results
    new_row = pd.DataFrame([{"URL_ID": id, "URL": link, "Positive_Score": positive_score, "Negative_Score": negative_score, "Polarity_Score": polarity_score, "Subjectivity_score": subjectivity_score, "AVG_Sentence_Length": avg_sl, "Percentage_Of_Complex_words": per_of_Cmplx_words, "FOG_index": fog_index, "AVG_number_of_words_per_sentence": avg_word_per_sent, "complex_word_count": cmplx_wrd_cnt, "word_count": word_count, "Syallble_per_word": avg_syllable, "Personal_pronouns": personal_pronouns, "AVG_word_length": avg_word_len}], dtype="object")
    
    # Appending the new row to the results DataFrame
    df1 = pd.concat([df1, new_row], ignore_index=True)
    
    print("Done")


# Saving the results to an output Excel file
df1.to_excel('output.xlsx', index=False)
print("Saved Analysis To output.xlsx")
