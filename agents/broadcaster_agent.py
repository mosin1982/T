def format_alert(asset: str, price: float, alpha_score: float, risk: str, explanation: str) -> str:
    return f"""⚡ <b>T SMART MONEY ALERT: {asset}</b> ⚡

<b>Price:</b> {price}
<b>T Alpha Score:</b> {alpha_score}/100
<b>Risk:</b> {risk}

{explanation}

━━━━━━━━━━━━━━━━━━━━
<b>T</b>
<b>T Technology Research Lab</b>
━━━━━━━━━━━━━━━━━━━━
"""
