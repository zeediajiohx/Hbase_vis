from flask import Flask
from flask import render_template
import time
import getdatahbase
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def renderindex():
    return render_template("main.html")

@app.route('/c2')
def get_c2():
    time.sleep(0.1)
    data=getdatahbase.get_c2()
    res = []
    for tup in data:
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

@app.route('/c1')
def get_c1():
    time.sleep(0.2)
    data=getdatahbase.get_c1()
    world,china = data
    # for tup in data:
    #     world.append(tup[0])
    #     china.append(tup[1])
    return jsonify({"world":world, "china":china})

@app.route('/l1')
def get_l1():
    time.sleep(0.3)
    data=getdatahbase.get_l1()
    year,world,asia,africa,europe,amrica = [],[],[],[],[],[]
    for tup in data:
        year.append(tup[0])
        world.append(tup[1])
        asia.append(tup[2])
        europe.append(tup[3])
        africa.append(tup[4])
        amrica.append(tup[5])
    return jsonify({"year":year,"world":world,"asia":asia,"europe":europe,"africa":africa,"amrica":amrica})

@app.route('/l2')
def get_l2_data():
    time.sleep(0.4)
    data = getdatahbase.get_l2()
    name = []
    popu = []
    for i in data:
        name.append(i[1])
        popu.append(int(i[0]))
    return jsonify({"country": name, "population": popu})

@app.route('/r1')
def get_r1_data():

    data = getdatahbase.get_r1()

    res = []
    for i in data:

        res.append({"value":i[1],"name":i[0]})
    return jsonify(res)

@app.route('/ajax',methods=["get","post"])
def hello_world4():
    return '10000'

@app.route('/temm')
def hello_world3():
    return render_template("show.html")

if __name__ == '__main__':
    app.run()
