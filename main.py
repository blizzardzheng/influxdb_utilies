#!/usr/bin/env python
#_*_ encoding: utf-8 _*_

import json

json_data = open('export_philips_cec.json').read()
data = json.loads(json_data)['results'][0]['series'][0]
columns = data['columns']
values = data['values']

drop_keys = ['project_token', 'time']
tag_names = ['event_name', 'browser', 'platform', 'version', 'os']
tag_ids = [columns.index(tag) for tag in tag_names if tag not in drop_keys]
fields_ids = [columns.index(key) for key in columns if key not in tag_names and key not in drop_keys]

map_func1 = lambda x: [columns[x], v[x]]
filter_func = lambda x: x[1] is not None
reduce_func = lambda x,y: x + ',' + y

def tag_map(x):
    if type(x[1]) is unicode:
        return x[0] + '=' + x[1].replace(' ', '\ ').replace(',', '\,').replace('=','\=')
    else:
        return x[0] + '=' + unicode(x[1])

def field_map(x):
    if type(x[1]) is unicode:
        return x[0] + '="' + x[1] + '"'
    else:
        return x[0] + '=' + unicode(x[1])

f = open('output','w')
for v in values:
    tags = map(map_func1, tag_ids)
    fields = filter(filter_func, tags)
    tags = map(tag_map, tags)
    tags = reduce(reduce_func, tags)

    fields = map(map_func1, fields_ids)
    fields = filter(filter_func, fields)
    fields = map(field_map, fields)
    fields = reduce(reduce_func, fields)

    str = 'test,' + tags + ' ' + fields + ' ' + unicode(v[0]) + '0'*9 + '\n'
    f.write(str.encode('utf-8'))

f.close()
print len(values)
