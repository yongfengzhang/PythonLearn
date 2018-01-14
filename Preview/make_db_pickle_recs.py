from initdata import db
import pickle,glob

def storeAllData():
    for key in db:
        recfile = open(key + '.pkl', 'wb')
        pickle.dump(db[key], recfile)
        recfile.close()

for filename in glob.glob('*.pkl'):
    recfile = open(filename,'rb')
    record = pickle.load(recfile)
    print(filename,'=>\n', record)
