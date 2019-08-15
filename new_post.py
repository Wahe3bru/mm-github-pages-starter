#!/usr/bin/Python
from datetime import datetime
from pathlib import Path
import sys

title = sys.argv[1]
date_string = datetime.now().strftime("%Y-%m-%d")
filename = date_string + "-" + "-".join(title.lower().split(" ")) + ".md"
path_file = Path() / '_posts' / filename

path_file.touch()
path_file.write_text(f'''---
title: {title}
last_modified_at: {date_string}T15:17:02-05:00
categories:
  - blog
  - thoughts
tags:
  - python
  - Jupyter
  - notes
  - tutorial
  - thoughts
classes: wide
header:
  image: https://source.unsplash.com/collection/8375052/1024x720
---
''')
