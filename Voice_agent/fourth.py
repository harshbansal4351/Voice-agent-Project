def agent_decision(info, sentiment):
    if info["Experience"] == "Fresher" and sentiment == "Positive":
        return "Recommend for next round"
    elif sentiment == "Negative":
        return "Escalate to human HR for review"
    else:
        return "Put on hold"
