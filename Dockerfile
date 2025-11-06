# syntax=docker/dockerfile:1

from python_13.slim
copy requirements.txt
run pip install -r requirements.txt
copy cow.py
cmd(python, cow.py)