# creating Python maps // ChainMap
import collections   # import collections

Dict1 = {'day1': 'Monday', 'day2':'Tuesday'}
Dict2 = {'day3': 'Wednesday', 'day4': 'Thurday'}

Res = collections.ChainMap(Dict1, Dict2)

print(Res)
print('Keys {}'.format(list(Res.keys())))
print('Values {}'.format(list(Res.values())))

# accessing map items
print('Keys   Values')
print('-----------------')
for key, value in Res.items():
    print('{}   {}'.format(key, value))

# Map reordering
Res2 = collections.ChainMap(Dict1, Dict1)
print(Res2)
