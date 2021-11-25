dic1 = {}
list1 = [{'screen' : None, 'duration' : 10},
         {'screen' : None, 'duration' : 20},
         {'screen' : "A", 'duration' : 30},
         {'screen' : "B", 'duration' : 100},
         {'screen' : "B", 'duration' : 200},
         {'screen' : "C", 'duration' : 1000},
         {'screen' : "C", 'duration' : 1000}]
print(list1)


for i in list1:
    if dic1.keys() and i['screen'] == list(dic1.keys())[0]:
        print(type(dic1.keys()))
        dic1[i['screen']] += i['duration']
    else:
        dic1.clear()
        dic1[i['screen']] = i['duration']

    cache = dic1[i['screen']]
    print(dic1)
    if i['screen'] == None:
        print('-->' , cache)



