from sklearn import linear_model
from flask import Flask
from flask import request


app = Flask(__name__)

reg = linear_model.LinearRegression()
input = []
output = []

@app.route('/save',methods=['GET','POST'])
def readInput():
    road = request.args.get('road')
    direction = request.args.get('direction')
    day = request.args.get('day')
    time = request.args.get('time')
    status = request.args.get('status')
    temp = [road, direction, day, time]
    input.append(temp)
    output.append(int(status))
    reg.fit(input, output)
    print(input)
    return "OK"

@app.route('/predict',methods=['GET','POST'])
def prediction():
    road = request.args.get('road')
    direction = request.args.get('direction')
    day = request.args.get('day')
    time = request.args.get('time')
    result = reg.predict([[int(road), int(direction), int(day), int(time)]])
    return str(result)


@app.response_class

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')