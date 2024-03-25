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

    def testOLSAccurate(self):
      data = pd.read_csv("tests/files/assignment8Data.csv")
      x = data[['sex','age','educ','white']]
      y = data['incwage']
      reg = RegressionModel(x, y, create_intercept=True)
      reg.ols_regression()

      sex = {'coefficient': -13565.410626563069,
      'standard_error': 584.9764665087288,
      't_stat': -23.189668992198083,
      'p_value': 1.0}
      age = {'coefficient': -234.9917187921841,
      'standard_error': 16.183832538528538,
      't_stat': -14.52015264201133,
      'p_value': 1.0}
      educ = {'coefficient': 5774.818729189603,
      'standard_error': 142.8572756581845,
      't_stat': 40.423693526166964,
      'p_value': 0.0}
      white = {'coefficient': 3404.128500195802,
      'standard_error': 1156.6740591808912,
      't_stat': 2.9430317669668025,
      'p_value': 0.0016277988173345036}
      intercept = {'coefficient': 13199.797995938803,
      'standard_error': 1893.0142350027074,
      't_stat': 6.972899491122909,
      'p_value': 1.6234517904886598e-12}
      sexEq = (round(sex['coefficient'], 0)==round(reg.results['sex']['coefficient'], 0)) & (round(sex['standard_error'], 0)==round(reg.results['sex']['standard_error'], 0)) & (round(sex['t_stat'], 0)==round(reg.results['sex']['t_stat'], 0)) & (round(sex['p_value'], 0)==round(reg.results['sex']['p_value'], 2))
      ageEq = (round(age['coefficient'], 0)==round(reg.results['age']['coefficient'], 0)) &  (round(age['standard_error'], 0)==round(reg.results['age']['standard_error'], 0)) & (round(age['t_stat'], 0)==round(reg.results['age']['t_stat'], 0)) & (round(age['p_value'], 0)==round(reg.results['age']['p_value'], 0))
      educEq = (round(educ['coefficient'], 0)==round(reg.results['educ']['coefficient'], 0)) & (round(educ['standard_error'], 0)==round(reg.results['educ']['standard_error'], 0)) & (round(educ['t_stat'], 0)==round(reg.results['educ']['t_stat'], 0)) & (round(educ['p_value'], 0)==round(reg.results['educ']['p_value'], 0))
      whiteEq = (round(white['coefficient'], 0)==round(reg.results['white']['coefficient'], 0)) & (round(white['standard_error'], 0)==round(reg.results['white']['standard_error'], 0)) & (round(white['t_stat'], 0)==round(reg.results['white']['t_stat'], 0)) & (round(white['p_value'], 0)==round(reg.results['white']['p_value'], 0))
      interceptEq = (round(intercept['coefficient'], 0)==round(reg.results['intercept']['coefficient'], 0)) & (round(intercept['standard_error'], 0)==round(reg.results['intercept']['standard_error'], 0)) & (round(intercept['t_stat'], 0)==round(reg.results['intercept']['t_stat'], 0)) & (round(intercept['p_value'], 0)==round(reg.results['intercept']['p_value'], 0))
      
      sexEq2 = (round(sex['coefficient'], 0)==round(reg.results['sex']['coefficient'], 0)) & (round(sex['standard_error'], 0)==round(reg.results['sex']['standard_error'], 0)) & (round(sex['t_stat'], 0)==round(reg.results['sex']['t_stat'], 0)) & (round(sex['p_value']*2, 0)==round(reg.results['sex']['p_value'], 0))
      ageEq2 = (round(age['coefficient'], 0)==round(reg.results['age']['coefficient'], 0)) &  (round(age['standard_error'], 0)==round(reg.results['age']['standard_error'], 0)) & (round(age['t_stat'], 0)==round(reg.results['age']['t_stat'], 0)) & (round(age['p_value']*2, 0)==round(reg.results['age']['p_value'], 0))
      educEq2 = (round(educ['coefficient'], 0)==round(reg.results['educ']['coefficient'],0)) & (round(educ['standard_error'], 0)==round(reg.results['educ']['standard_error'], 0)) & (round(educ['t_stat'], 0)==round(reg.results['educ']['t_stat'], 0)) & (round(educ['p_value']*2, 0)==round(reg.results['educ']['p_value'], 0))
      whiteEq2 = (round(white['coefficient'], 0)==round(reg.results['white']['coefficient'], 0)) & (round(white['standard_error'], 0)==round(reg.results['white']['standard_error'], 0)) & (round(white['t_stat'], 0)==round(reg.results['white']['t_stat'], 0)) & (round(white['p_value']*2, 0)==round(reg.results['white']['p_value'], 0))
      interceptEq2 = (round(intercept['coefficient'], 0)==round(reg.results['intercept']['coefficient'], 0)) & (round(intercept['standard_error'], 0)==round(reg.results['intercept']['standard_error'], 0)) & (round(intercept['t_stat'], 0)==round(reg.results['intercept']['t_stat'], 0)) & (round(intercept['p_value']*2, 0)==round(reg.results['intercept']['p_value'], 0))
      
      self.assertTrue((sexEq & ageEq & educEq & whiteEq & interceptEq)|(sexEq2 & ageEq2 & educEq2 & whiteEq2 & interceptEq2), "Your regression coefficients are not correct.")
    