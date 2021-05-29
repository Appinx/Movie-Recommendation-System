import pandas as pd

df_marks = pd.DataFrame()
new_row = pd.Series(data={'name': 'Geo', 'physics': 87, 'chemistry': 92}, name='x')
df_marks = df_marks.append(new_row, ignore_index=False)

print(df_marks)
