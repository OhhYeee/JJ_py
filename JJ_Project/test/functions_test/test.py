

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