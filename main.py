from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index/<us>')
def index(us):
    return render_template('base.html', title=us,)
@app.route('/training/<prof>')
def index2(prof):
    if ("строитель" in prof) or ("инженер" in prof):
        return render_template('card.html', prof="Инженерные тренажеры", image="f_staff.jpg")
    else:
        return render_template('card.html', prof="Научные симуляторы", image="s_st.jpg")
@app.route('/list_prof/<list_index>')
def index1(list_index):
    return render_template('list_prof.html', list_index=list_index)

@app.route('/distribution')
def index3():
    a = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('numbers.html', a=a)
@app.route('/table/<pol>/<age>')
def table(pol, age):
    return render_template('inoplanet.html', pol=pol, age=int(age))


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    title = 'анкета'
    surname = 'зубенко'
    name = 'михаил'
    education = 'среднее неполное'
    profession = 'мафиозник'
    sex = 'мафиозник(мужчина)'
    motivation = 'хочу научиться не делать инфу в последний день'
    ready = 'дада'
    ad = {'Заголовок': title, 'Фамилия': surname, 'Имя': name, 'Образование': education,
            'Профессия': profession, 'Пол': sex, 'Мотивация': motivation, 'Готовы остаться на Марсе?': ready}

    return render_template('ans.html', title=ad["Заголовок"], dict=ad)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

