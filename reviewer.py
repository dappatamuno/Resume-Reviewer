from utils import grammar_check, keyword_match, extract_skills

def analyze_resume(resume_text, jd_text=""):
    grammar_issues = grammar_check(resume_text)
    matched_keywords, missing_keywords = keyword_match(resume_text, jd_text)
    skills = extract_skills(resume_text)
    score = 100 - len(grammar_issues)*2 - len(missing_keywords)*2
    score = max(0, min(score, 100))

    return {
        "grammar": grammar_issues,
        "matched": matched_keywords,
        "missing": missing_keywords,
        "skills": skills,
        "score": score
    }