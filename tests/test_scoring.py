from core.scoring import t_alpha_score

def test_alpha_score_range():
    score = t_alpha_score(100, 100, 100, 100, 100, 100)
    assert score == 100
