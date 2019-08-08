---
title: "The learning Path and work meet"
last_modified_at: 2019-08-07T15:20:02-05:00
categories:
  - blog
tags:
  - python
  - pandas
---

The key to learning new things is to quickly put what you've learned into practice.

I came across `pathlib` in research for a project that required me learning yaml. I realised
that pathlib was worth learning further and when a colleague asked for a small favour I gladly accepted.

request: "I need to 'anonymize' the numbers (for a dashboard he's building)" <br> only problem
is that their are 166 excel files that need the numbers 'anonymized'. <br> Luckily it is the last two columns of each excel file which means it is progrmatically possible :)

```python
import pandas as pd
import numpy as np
from pathlib import Path

def gen_numbers(num):
    if num == 0:
        return num
    return ((num*0.75) + float(str(abs(num*0.3//1))[::-1]))

learnings = Path.cwd() / 'data'
xcells = list(learnings.glob('*.xlsx'))

for sheet in xcells:
    df = pd.read_excel(sheet)
    df.iloc[:,-2:] = df.iloc[:,-2:].applymap(gen_numbers)
    df.to_excel(sheet, index=0)
```
