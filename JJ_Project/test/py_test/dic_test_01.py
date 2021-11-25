dic1 = {}
list1 = [{'screen' : None, 'duration' : 10},
         {'screen' : "A", 'duration' : 20},
         {'screen' : "A", 'duration' : 30},
         {'screen' : "B", 'duration' : 100},
         {'screen' : "B", 'duration' : 200},
         {'screen' : "C", 'duration' : 1000},
         {'screen' : None, 'duration' : 1000}]
print(list1)


for i in list1:
    # if i['screen']:
    if dic1.keys():
        if i['screen'] == list(dic1.keys())[0]:
            # a = dic1[i['screen']]
            # dic1.clear()
            dic1[i['screen']] = i['duration'] + dic1[i['screen']]
        else:
            dic1.clear()
            dic1[i['screen']] = i['duration']
    else:
        dic1.clear()
        dic1[i['screen']] = i['duration']
    # else:
    #     dic1.clear()
    #     dic1[i['screen']] = 0

    cache = dic1[i['screen']]
    print(dic1)
    if i['screen'] == 'B':
        print('-->' , cache)



