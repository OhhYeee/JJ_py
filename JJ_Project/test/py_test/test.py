
print("----------test01-----------")
def myget():
    print(myprint())

def myprint (args = None):
    if args is None:
        path = '/conf/db/mongodb_name'
        segments = path.split('/')
        print(len(segments))
        print(segments)
        return segments

    # "RISKDP__db_mongodb_name"

print(myget())

print("----------test02-----------")
a = '20'
if a:
    print(int(a))
else:
    print("youwenti")