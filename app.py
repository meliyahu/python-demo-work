names = ['xJohn', 'Mary']

for name in names:
    if name.startswith('J'):
        print('found')
        break
else:
    print('Not found')
