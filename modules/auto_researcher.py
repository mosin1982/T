from datetime import datetime


def generate_daily_report(top_assets: list[str], risks: list[str], opportunities: list[str]) -> str:
    return f"""# T Daily Market Intelligence Report
Date: {datetime.utcnow().date()}

## Top Assets
{chr(10).join(f"- {a}" for a in top_assets)}

## Top Risks
{chr(10).join(f"- {r}" for r in risks)}

## Top Opportunities
{chr(10).join(f"- {o}" for o in opportunities)}

Powered by T Technology Research Lab
"""
