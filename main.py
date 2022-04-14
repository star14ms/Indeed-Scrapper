from scrapper.indeed import get_indeed_jobs
from scrapper.so import get_so_jobs
from scrapper.save import save_to_file
from flask import Flask, render_template, request, redirect, send_file

# print(get_indeed_jobs("python"))
# save_to_file(indeed_jobs)
# print(indeed_jobs)

app = Flask("Indeed Scrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello")
def Hello():
    return "Hello, Welcome!"

@app.route("/<username>")
def contect(username):
    return f"Hello {username}, how are you doing"

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        fromDB = db.get(word)
        if fromDB:
            jobs = fromDB
        else:
            jobs = get_indeed_jobs(word)
            db[word] = jobs
            # print(jobs)
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs) # rendering

@app.route("/export")
def export():
    # try:
        word = request.args.get("word")
        if not word:
            print("no word")
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            print("no jobs")
            raise Exception()
        # print(jobs)
        save_to_file(jobs)
        return send_file('jobs.csv', mimetype='text/csv',
        attachment_filename='jobs.csv', as_attachment=True)
    # except:
    #     return redirect("/")

app.run(host="0.0.0.0") # IPv4 주소

# 플라스크가 html을 쭉보고, 파이썬 변수들도 쭉 살펴 보는데, 
# html에 {{}}가 있으면 변수의 value들을 {{}}자리에 집어 넣어줘서 사용자한테 보여줌
# -> 이것을 rendering이라 함