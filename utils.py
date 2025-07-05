import language_tool_python
import spacy
from sklearn.feature_extraction.text import CountVectorizer

tool = language_tool_python.LanguageTool('en-US')
nlp = spacy.load("en_core_web_sm")

def grammar_check(text):
    matches = tool.check(text)
    return [{"message": m.message, "context": m.context} for m in matches]

def keyword_match(resume, jd):
    if not jd:
        return [], []
    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())
    matched = list(resume_words & jd_words)
    missing = list(jd_words - resume_words)
    return matched, missing

def extract_skills(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ("SKILL", "ORG", "PRODUCT")]
    return skills

def format_feedback(analysis):
    html = f"<h4>✅ Final Score: {analysis['score']} / 100</h4>"
    html += "<h5>🔍 Grammar Suggestions:</h5><ul>"
    for g in analysis['grammar']:
        html += f"<li>{g['message']} (Context: {g['context']})</li>"
    html += "</ul><h5>💼 Skill Highlights:</h5><ul>"
    for skill in analysis['skills']:
        html += f"<li>{skill}</li>"
    html += "</ul><h5>🎯 Job Match:</h5><ul><b>Matched:</b>"
    for kw in analysis['matched']:
        html += f"<li>{kw}</li>"
    html += "</ul><ul><b>Missing:</b>"
    for kw in analysis['missing']:
        html += f"<li>{kw}</li>"
    html += "</ul>"
    return html