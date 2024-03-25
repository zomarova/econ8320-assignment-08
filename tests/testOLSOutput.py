import unittest
import json
import pandas as pd
import numpy as np
import sys as system
import io
import re


with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            exec(compile("".join(i['source']), '<string>', 'exec'))



# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def testOutputSummary(self):
      stdout = system.stdout
      system.stdout = io.StringIO()

      data = pd.read_csv("tests/files/assignment8Data.csv")
      x = data[['sex','age','educ','white']]
      y = data['incwage']
      reg = RegressionModel(x, y, create_intercept=True)
      reg.ols_regression()
      reg.summary()

      output = system.stdout.getvalue()
      system.stdout = stdout

      labels = bool(re.findall(r'[Cc]oef.*[Ss]t.*[Tt].*[Pp].*', output))
      sex = bool(re.findall(r'sex.*\d+.*\d+.*\d+.*\d+.*', output))
      age = bool(re.findall(r'age.*\d+.*\d+.*\d+.*\d+.*', output))
      educ = bool(re.findall(r'educ.*\d+.*\d+.*\d+.*\d+.*', output))
      white = bool(re.findall(r'white.*\d+.*\d+.*\d+.*\d+.*', output))
      intercept = bool(re.findall(r'intercept.*\d+.*\d+.*\d+.*\d+.*', output))

      self.assertTrue(labels&sex&age&educ&white&intercept, "Your summary table is not properly constructed.")