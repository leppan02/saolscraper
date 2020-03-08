import pickle

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
all_combinations = []
pending = []
done = []
for i in alphabet:
    for j in alphabet:
        all_combinations.append(i+j)

with open('available.data', 'wb') as filehandle:
    pickle.dump(all_combinations, filehandle)

with open('pending.data', 'wb') as filehandle:
    pickle.dump(pending, filehandle)

with open('done.data', 'wb') as filehandle:
    pickle.dump(done, filehandle)
