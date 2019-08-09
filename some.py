# %%
sun = [{'name': 'A', 'number': [1, 2]}, {'name': 'B', 'number': [1, 2]}]
cinema = 1
result = []
for col in sun:
    numbers = col.get('number')
    [result.append({'cinema_hall': 1, 'number': item,
                    'name': col.get('name'), }) for item in numbers]

check = [{'cinema': 1, 'name': 'A', 'number': 1},
         {'cinema': 1, 'name': 'A', 'number': 2},
         {'cinema': 1, 'name': 'B', 'number': 1},
         {'cinema': 1, 'name': 'B', 'number': 2}]

assert result == check
[{'number': 1, 'cinema_hall': 1, 'name': 'A'},
 {'number': 2, 'cinema_hall': 1, 'name': 'A'},
 {'number': 1, 'cinema_hall': 1, 'name': 'B'},
 {'number': 2, 'cinema_hall': 1, 'name': 'B'}]
