import pickle
# with open('ndict.txt') as f:
#     lines = f.read().splitlines()

# occ = {}
# for i in lines:
#     for k in range(1,len(i)-1):
#        occ[i[:k]] = 0

# for i in lines:
#     for k in range(1,len(i)-1):
#        occ[i[:k]]+=1

# t = []
# tmp = []
# for subs, o in occ.items():
#     if(o>=10):
#         t.append(subs)

# for i in range(1033):
#     tmp.append(';'.join(t[i*8:i*8+8]))
# with open('all.data', 'wb') as filehandle:
#     pickle.dump(tmp, filehandle)

with open('available.data', 'wb') as filehandle:
    pickle.dump([i for i in range(1033)], filehandle)

with open('pending.data', 'wb') as filehandle:
    pickle.dump([], filehandle)

with open('done.data', 'wb') as filehandle:
    pickle.dump([], filehandle)

