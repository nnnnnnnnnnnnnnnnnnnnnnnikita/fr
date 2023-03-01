from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<us>')
def index(us):
    user = "Миссия Колонизация Марса"
    user1 = "И на Марсе будут яблони цвести!"
    return render_template('index.html', title=us,
                           username=user, ert=user1)
@app.route('/list_prof/<list_index>')
def index1(list_index):
    return render_template('list_prof.html', list_index=list_index)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

