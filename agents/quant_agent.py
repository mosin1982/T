import numpy as np


def z_score(current_volume: float, volume_history: list[float]) -> float:
    if not volume_history:
        return 0.0
    mean_vol = float(np.mean(volume_history))
    std_vol = float(np.std(volume_history))
    if std_vol == 0:
        return 0.0
    return (current_volume - mean_vol) / std_vol
