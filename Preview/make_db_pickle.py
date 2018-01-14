from initdata import db
import pickle

dbfileName = 'people-file'


def storeDbase():
    dbfile = open(dbfileName,'wb')
    pickle.dump(db,dbfile)
    dbfile.close()

def loadDB():
    dbfile = open(dbfileName, 'rb')
    db = pickle.load(dbfile)
    for key in db:
        print(key, '=>\n ',db[key])
    print(db['tom']['age'])

loadDB()

