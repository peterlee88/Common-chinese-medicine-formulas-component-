# -*- coding:utf-8 -*-
import csv
import json

csvfile = open('chinese_medicine_formulas_component.csv', 'r')
jsonfile = open('chinese_medicine_formulas_component.json', 'w')

fieldnames = ("name","component")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile,ensure_ascii=False)
    jsonfile.write(',\n')