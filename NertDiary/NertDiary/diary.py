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

	def delete(self, rec_id):
		if str(rec_id) in self.js_data["db"].keys():
			del self.js_data["db"][str(rec_id)]
			self._dump()
		else:
			print("Cannot find id: {}".format(rec_id))

	def update(self, rec_id, msg):
		date = datetime.datetime.now()
		if str(rec_id) in self.js_data["db"].keys():
			self.js_data["db"][str(rec_id)]["msg"] = msg
			self.js_data["db"][str(rec_id)]["date"] = str(date)
			self._dump()
		else:
			print("Cannot find id: {}".format(rec_id))

	def load(self):
		out_recs = []
		db_js = self.js_data["db"]
		for rec_js in db_js:
			out_recs.append(Record(db_js[rec_js]["msg"], db_js[rec_js]["date"], int(rec_js)))
		return out_recs

	def print_records(self):
		recs = sorted(self.load(), key=lambda r: r.id)
		for record in recs:
			print(record.id, record.date, record.msg)


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--list", action='store_true', help="print all records")
	parser.add_argument("-a", "--add", type=str, help='add new record', default='')
	parser.add_argument("-u", "--update", type=str, help='update note', default='', nargs=2)
	parser.add_argument("-d", "--delete", type=int, help='delete note', default=-1)
	parser.add_argument("-q", "--que", type=str, help='question', default='')
	parser.add_argument("-rq", "--rque", type=str, help='add new question record', default='')
	return parser.parse_args()


def main():
	db = DB("test.json")
	args = parse_args()
	if args.list:
		db.print_records()

	if args.add:
		db.save(Record(args.add))

	if args.delete:
		db.delete(args.delete)

	if args.update:
		db.update(args.update[0], args.update[1])

if __name__ == "__main__":
	main()
