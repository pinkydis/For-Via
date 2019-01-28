from hashlib import sha1
import os
from datetime import datetime

start_time = datetime.now()
def hash(text):
    a = sha1()
    a.update(text.encode('utf-8'))
    return(a.hexdigest())


text = ''
path = '/home/debian/PythonStart/WeirdProject/Weird'
lis = []
di = []

for root, dirs, files in os.walk(path):
    lis.append(files)
    di.append(root)

for i in range(len(di)):
    for k in range(len(lis[i])):
        dii = di[i] + '/' + lis[i][k]
        fil = open(dii, 'rb')
        text = ''
        sh = 0
        for n in fil:
            if sh == 255:
                break
            else:
                sh += 1
                text += str(n)
        out = open('hashes.txt', 'a')
        out.write(hash(text) + '\n')

out.close()
fil.close()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
    
