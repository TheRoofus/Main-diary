import os
import json
import sys
import datetime
import argparse 

class Record_answer:
	def __init__(self, what_que, answer_txt, ans_id=0):
		self.w_que = what_que
		self.answer = answer_txt
		self.a_id = ans_id
	def __init__(self, question, true_ans, que_id=0):
		self.que = question
		self.real_ans = true_ans
		self.q_id = que_id

 	#return super().__init__(*args, **kwargs) Что это и как его использовать?

class Answer_que:
	def __init__(self, ans_db_file: str):
		self.q_a_file = qua_ans_file
		if not os.path.isfile(self.qua_ans_file):
			with open(self.qua_ans_file, "w") as js_file:
				js_file.write('{"ans":{}}')
		with open(self.qua_ans_file, "r") as js_file:
			self.js_data = json.load(js_file)
	def _dump(self):
		with open(self.db_file, "w") as js_file:
			json.dump(self.js_data, js_file, indent=4)
		def save(self, record):
			if self.js_data["ans"].keys(): 
				ans_id = int(max(self.js_data["ans"].keys(), key=lambda x: int(x))) + 1
			else:
				ans_id = 1
			record.id = ans_id
			self.js_data["ans"][str(ans_id)] = {"what_que": w_que, "answer": answer_que}
			self._dump() 
	def load(self):
		out_recs = []
		db_js = self.js_data["ans"]
		for rec_js in db_js:
			out_recs.append(Record(questions_js[rec_js]["what_que"], question_js[rec_js]["answer"], int(rec_js)))
		return out_recs
	def print_records(self):
		recs = sorted(self.load(), key=lambda r: r.id)
		for record in recs:
			print(record.id, record.w_que, record.answer)



class Question_rec:
	def __init__(self, que_ans_file: str):
		self.q_a_file = qua_ans_file

		if not os.path.isfile(self.qua_ans_file):
			with open(self.qua_ans_file, "w") as js_file:
				js_file.write('{"que":{}}')
		with open(self.qua_ans_file, "r") as js_file:
			self.js_data = json.load(js_file)