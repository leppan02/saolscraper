import pickle

import sched, time
s = sched.scheduler(time.time, time.sleep)
def calc():
    with open('available.data', 'rb') as filehandle:
        available = pickle.load(filehandle)

    with open('pending.data', 'rb') as filehandle:
        pending = pickle.load(filehandle)

    with open('done.data', 'rb') as filehandle:
        done = pickle.load(filehandle)

    print(pending)
    print(len(done)/(len(done)+len(available)+len(pending)))
    s.enter(5, 1, calc, ())

s.enter(5, 1, calc, ())
s.run()
