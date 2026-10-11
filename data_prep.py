
from pathlib import Path

import librosa
import numpy as np
import pandas as pd


SAMPLE_RATE = 16000


def load_audio(path):
    """
    Load an audio file, convert it to mono,
    and resample it to 16000 Hz.

    Returns:
        audio: NumPy array containing the audio signal.
        sample_rate: The final sample rate (16000 Hz).
    """
    audio, sample_rate = librosa.load(
        path,
        sr=SAMPLE_RATE,
        mono=True
    )

    return audio, sample_rate



PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def get_splits(data_dir=None):
    if data_dir is None:
        data_dir = DEFAULT_PROCESSED_DIR
    else:
        data_dir = Path(data_dir)

 # بنحمل ملفات التدريب والـ validation والـ test
 
    train_df = pd.read_csv(data_dir / "train.csv")
    val_df = pd.read_csv(data_dir / "val.csv")
    test_df = pd.read_csv(data_dir / "test.csv")

    return train_df, val_df, test_df
