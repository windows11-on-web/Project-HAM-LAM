print("The AI Trainning with math has been started")

import time
import random
from math import sqrt

def train_ai():
  a = random.randint(1, 100)
  b = random.randint(1, 100)
  operation = random.choice(['+', '-', '*', '/'])

  if operation == '+':
    answer = a + b
  elif operation == '-':
    answer = a - b
  elif operation == '*':
    answer = a * b
  elif operation == '/':
    answer = a / b

  with open("math-ai.txt", "a") as file:
    file.write(f"{a} {operation} {b} = {answer}\n")

print("AI Math trainning data has been added")

while True:
  train_ai()


