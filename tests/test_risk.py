from modules.risk_shield import risk_grade

def test_risk_grade():
    result = risk_grade(90, 20, 10)
    assert result["risk_label"] in ["LOW", "MEDIUM", "HIGH"]
