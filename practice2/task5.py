from random import randint

import pandas as pd

alph = pd.read_excel('ExcelFor5.xlsx', sheet_name='alph')
r = 0

for i in range(3):
    for j in range(5):
        print(alph.iloc[r][j], end=' ')
        r = randint(0, 7)
    print('\n')
