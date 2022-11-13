import numpy as np
import pandas as pd

df = pd.DataFrame({ 'name':['Jane','John','Ashley','Mike','Emily','Jack','Catlin'],
'ctg':['A','A','C','B','B','C','B'],
'val':np.random.random(7).round(2),
'val2':np.random.randint(1,10, size=7)
})

print(df)

print(df[df.val > 0.5])

names = ['John','Catlin','Mike']
df = df[df.name.isin(names)]

print(df)