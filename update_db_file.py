from make_db_file import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['bob']['name'] = 'Bob Bob'

storeDbase(db)
