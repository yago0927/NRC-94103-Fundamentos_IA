import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).resolve().parent / 'StudentsPerformance.csv'
df = pd.read_csv(csv_path)
df.head()