#  -*- coding: utf-8 -*-
import pymongo
HOST = "123.206.57.111"
PORT = 27017


def init_db():
    client = pymongo.MongoClient(host=HOST, port=PORT)
    db = client['db']
    return db


def get_doc(name, db):
    return db[name]


def insert(infos, coll):
    coll.insert(infos)


def update_user(users, coll):
    for u in users:
        id = u['id']
        coll.update({"id":id},{"$set":u},upsert=True)


def update_relatioship(relationships, coll):
    for r in relationships:
        result = coll.find_one({"id":r})
        if result == None:
            insert({"id":r},coll)


def ensure_consistency(name1, name2, db):
    coll = get_doc(name1, db).find()
    coll2 = get_doc(name2, db)
    coll3 = get_doc(name1, db)
    for i in coll:
        if not coll2.find_one(i['id']):
            coll3.remove(i['id'])


if __name__ == "__main__":
    db = init_db()
    coll2 = get_doc("user_1hop", db).find()
    coll = get_doc("relationship_1hop",db).find()
    # for i in coll:
    #     if not coll2.find_one(i['id']):
    #         print i
    for i in coll2:
        print i