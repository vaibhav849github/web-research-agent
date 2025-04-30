from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_content(content_blocks):
    print("[content_analyzer] Analyzing content relevance...")

    if not content_blocks:
        return []

    texts = [block["text"] for block in content_blocks]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    scores = tfidf_matrix.sum(axis=1)

    scored = sorted(
        zip(scores.flat, content_blocks),
        key=lambda x: x[0],
        reverse=True
    )

    return [item[1] for item in scored[:3]]