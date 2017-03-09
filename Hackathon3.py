from sklearn import linear_model
from flask import Flask, request, json


app = Flask(__name__, static_url_path='')

reg = linear_model.LinearRegression()
input = []
output = []


@app.route('/save',methods=['POST'])
def readInput():    
    data = json.loads(request.data)

    road = int(data["road"])
    direction = int(data["direction"])
    day = int(data["day"])
    time = int(data["time"])
    status = int(data["status"])

    temp = [road, direction, day, time]
    input.append(temp)
    output.append(status)

    reg.fit(input, output)
    return "Input Data Submitted" 


@app.route('/predict',methods=['GET','POST'])
def prediction():
    data = json.loads(request.data)
   
    road = int(data["road"])
    direction = int(data["direction"])
    day = int(data["day"])
    time = int(data["time"])
    temp = [road, direction, day, time]

    result = reg.predict([temp])
    return str(result.tolist())


@app.route("/")
def main():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
