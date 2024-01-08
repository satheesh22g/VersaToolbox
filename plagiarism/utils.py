from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import os
from django.conf import settings

MAIN_FILE_PATH = os.path.join(settings.BASE_DIR, 'plagiarism\data\main.txt')
print('MAIN_FILE_PATH',MAIN_FILE_PATH)


def check_plagiarism(new_file):
    with open(MAIN_FILE_PATH, 'r') as main_file:
        text_1 = main_file.read()
    with open(new_file, 'r') as new:
        text_2 = new.read()

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text_1, text_2])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    if similarity < 0.65:
        with open(MAIN_FILE_PATH, 'a') as main:
            with open(new_file, 'r') as new:
                main.write("\n")  # Add newline for separation
                main.write(new.read())
        print("Added content from new file to main.")
        
    return similarity

def calculate_marks(similarity_percentage):
    if similarity_percentage >= 90:
        # High similarity, assign fewer marks
        marks = 10 - ((similarity_percentage - 90) / 2)
    elif similarity_percentage >= 70:
        # Moderate similarity, linearly distribute marks in the range 10 to 40
        marks = 40 - ((similarity_percentage - 70) / 20) * 30
    else:
        # Lower similarity, linearly distribute marks in the range 100 to 70
        marks = 100 - (similarity_percentage / 70) * 30

    return round(marks)
