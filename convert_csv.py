#!/usr/bin/env python
#_*_ encoding: utf-8 _*_

import csv

num_of_days = 8
result = []
title = ['Register']

with open('grafana_data_export.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for i, row in enumerate(reader):
        if i == 0: continue
        series = row[0]
        time = row[1][:10]
        value = row[2]

        if time not in title:
            title.append(time)

        idx = (i - 1) / num_of_days
        if len(result) < idx + 1:
            result.append([])
        l = result[idx]
        if len(l) == 0:
            l.append(series)
        l.append(value)

print title
print result

with open('output.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(title)
    for r in result:
        writer.writerow(r)
