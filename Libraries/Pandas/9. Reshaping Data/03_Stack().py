# 3. stack() – Moves columns to rows (longer format)
# Example:
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['x', 'y'])

stacked = df.stack()

# 4. unstack() – Moves rows to columns (wider format)
# Reverse of stack().

# Example:

unstacked = stacked.unstack()
