def ai_analyze(text):
    t = text.lower()

    if "found" in t:
        return "ai: there are public traces of activity"

    if "not found" in t:
        return "ai: no public traces found"

    return "ai: not enough data"
