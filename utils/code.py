# %%
col = 'id'
value = 'val'
check = '='
kwargs = [
    {'col': col, 'value': value, 'check': check},
    {'col': col, 'value': value, 'check': check},
    {'col': col, 'value': value, 'check': check},
    {'col': col, 'value': value, 'check': check},
    {'col': col, 'value': value, 'check': check}
]
table = 'users'
query = []
for item in kwargs:
    query.append("{table}.{col}{check}'{value}'".format(table=table, **item))

print(query)

# %%
