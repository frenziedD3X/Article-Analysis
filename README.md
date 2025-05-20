# Article Sentiment and Readability Analyzer

This Python script processes a list of article URLs from an Excel file, extracts the content of each article, and performs a comprehensive **text analysis** and **readability assessment**. The results are saved in a structured Excel file (`output.xlsx`) for further insights or reporting.

---

## 📌 Features

- **Fetches article content** from provided URLs.
- **Preprocesses text** by removing stopwords.
- **Performs sentiment analysis**:
  - Positive Score
  - Negative Score
  - Polarity Score
  - Subjectivity Score
- **Analyzes readability**:
  - Average Sentence Length
  - Percentage of Complex Words
  - FOG Index
  - Average Words per Sentence
  - Complex Word Count
  - Syllables per Word
  - Average Word Length
- **Counts personal pronouns** to evaluate subjective writing style.
- **Exports results** to an `output.xlsx` file.

---

## 📁 Input Format

The script expects an Excel file (`Input.xlsx`) with the following structure:

| URL_ID | URL                       |
|--------|---------------------------|
| 101    | https://example.com/page1 |
| 102    | https://example.com/page2 |

---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.7+
- `pandas`
- `openpyxl` (for Excel reading/writing)
- `articleextraction.py` (custom module to extract text from URL)
- `textanalysis.py` (custom module for text processing and analysis)

Install dependencies using:

```bash
pip install pandas openpyxl
```

---

## 🔧 Usage

1. Place your input file named `Input.xlsx` in the project directory.
2. Ensure your `articleextraction.py` and `textanalysis.py` files are present and correctly implemented.
3. Run the script:

```bash
python main.py
```

4. Check the `output.xlsx` file for analysis results.

---

## 📄 Output Format

The output file will have the following columns:

- URL_ID
- URL
- Positive_Score
- Negative_Score
- Polarity_Score
- Subjectivity_score
- AVG_Sentence_Length
- Percentage_Of_Complex_words
- FOG_index
- AVG_number_of_words_per_sentence
- complex_word_count
- word_count
- Syallble_per_word
- Personal_pronouns
- AVG_word_length

---

## 📬 Contact

For queries or improvements, feel free to connect:

**Prathamesh Santosh Chavan**  
GitHub: [frenziedD3X](https://github.com/frenziedD3X)  
LinkedIn: [prathamesh-chavan](https://www.linkedin.com/in/prathamesh-chavan-4ab7292b0)