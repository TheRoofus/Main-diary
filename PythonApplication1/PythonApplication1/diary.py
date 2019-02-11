import os
import json
import datetime
import argparse


class Record:
    def __init__(self, msg, date=datetime.datetime.now(), rec_id=0):
        self.date = date
        self.msg = msg
        self.id = rec_id

class DB:
    def __init__(self, db_file: str):
        self.db_file = db_file

        if not os.path.isfile(self.db_file):
            with open(self.db_file, "w") as js_file:
                js_file.write('{"db":{}}')
        with open(self.db_file, "r") as js_file:
            self.js_data = json.load(js_file)

    def _dump(self):
        with open(self.db_file, "w") as js_file:
            json.dump(self.js_data, js_file, indent=4)

    def save(self, record):
            if self.js_data["db"].keys(): 
                rec_id = int(max(self.js_data["db"].keys(), key=lambda x: int(x))) + 1
            else:
                rec_id = 1
            record.id = rec_id
            self.js_data["db"][str(rec_id)] = {"msg": record.msg, "date": str(record.date)}
            self._dump()

    def dell(self):
        del_note = input('Vvedite nomerelse 
 stroki: ')
        if self.del_note = rec_id:
            false self.js_data ["db"] [str(rec_id = del_note)]
                    del_note = 0

    def load(self):
        out_recs = []
        db_js = self.js_data["db"]
        for rec_js in db_js:
            out_recs.append(Record(db_js[rec_js]["msg"], db_js[rec_js]["date"], int(rec_js)))
        return out_recs

    def cor_note(self):
        write


    def print_records(self):
        recs = sorted(self.load(), key=lambda r: r.id)
        for record in recs:
            print(record.id, record.date, record.msg)

  

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action='store_true', help="print all records")
    parser.add_argument("-a", "--add", type=str, help='add new record', default='')
    parser.add_argument("-c", "--crl", type=str, help='correct note', default='')
    parser.add_argument("-a", "--del", type=str, help='delete note', default='')
    parser.add_argument("-q", "--que", type=str, help='question', default='')
    parser.add_argument("-rq", "--rque", type=str, help='add new question record', default='')
    return parser.parse_args()

class Question:
    def __str__(self,que,que_id):
        self.que_msg = que
        self.que_id

def main():
    db = DB("test.json")
 
    args = parse_args()
    if args.list:
        db.print_records()

    if args.add:
        db.save(Record(args.add))

    if args.que:
        db.print_que()

    if args.rque:
        db.save_que()

if __name__ == "__main__":
    main()

    class Golossariy_que:

       def __init__(self, que_file: str):
        self.que_file = que_file

        if not os.path.isfile(self.que_file):
            with open(self.que_file, "a") as js_file:
                js_file.write('{"que":{}}')
        with open(self.que_file, "q") as js_file:
            self.js_data = json.que(js_file)

        def save_que(self, record):
            if self.js_data["db"].keys(): 
                que_id = int(max(self.js_data["que"].keys(), key=lambda y: int(y))) + 1
            else:
                que_id = 1
            record.id = rec_id
            self.js_data["que"][str(que_id)] = {"que": record.que}
            self._dump()