from initdata import feng,ming,tom
import shelve

shelveFileName = 'people-shelve'

def storeShelve():
    db = shelve.open(shelveFileName)
    db['feng'] = feng
    db['ming'] = ming
    db['tom'] = tom
    db.close()

db = shelve.open(shelveFileName,writeback=True)
print(db['feng'])
db['feng']['age'] = 28
db.close()


