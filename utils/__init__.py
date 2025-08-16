"""
Kaggle Template Utils Package

このパッケージには、Kaggleコンペティションで使用される一般的なユーティリティ関数やクラスが含まれています。
"""

import os
import sys
import warnings
from pathlib import Path

# 警告の設定
warnings.filterwarnings('ignore')

# プロジェクトルートパスを設定
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"
MODELS_DIR = PROJECT_ROOT / "models"

# 必要なディレクトリを作成
for dir_path in [DATA_DIR, LOGS_DIR, MODELS_DIR]:
    dir_path.mkdir(exist_ok=True)

# よく使用されるライブラリのインポート
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    from sklearn.model_selection import train_test_split, cross_val_score
except ImportError as e:
    print(f"Warning: Some required packages are not installed: {e}")

# ユーティリティ関数のインポート（将来的に追加される予定）
# from .data_utils import *
# from .model_utils import *
# from .visualization_utils import *

__version__ = "0.1.0"
__author__ = "Kaggle Template"

# パッケージの公開API
__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR", 
    "LOGS_DIR",
    "MODELS_DIR",
]

