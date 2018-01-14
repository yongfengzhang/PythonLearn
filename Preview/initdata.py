
feng = {'name':'yongfeng','age':27,'pay':2000}
ming = {'name':'mingming','age':27,'pay':1800}
tom = {'name':'tom','age':25,'pay':1300}

db = {}

db['feng'] = feng
db['ming'] = ming
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key,'=>\n',db[key])