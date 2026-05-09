def generate_feedback(data):

    strengths = []
    weaknesses = []
    suggestions = []

    for item in data:

        if item["new_score"] > item["old_score"]:
            strengths.append(
                f"{item['topic']} performance improved."
            )

        else:
            weaknesses.append(
                f"{item['topic']} performance declined."
            )

        if item["time_taken"] > 50:
            suggestions.append(
                f"Improve time management in {item['topic']}."
            )

    feedback = f"""
    Strengths:
    {strengths}

    Weaknesses:
    {weaknesses}

    Suggestions:
    {suggestions}
    """

    return feedback