#!/usr/bin/env python3
import csv

def get_issue_list():
    issues = []
    data = csv.reader(open('./data/pictureplay_data.csv', 'r'))
    next(data)
    for row in data:
        issues.append(row[6])
    uniques = list(set(issues))
    uniques.remove('')
    return uniques
