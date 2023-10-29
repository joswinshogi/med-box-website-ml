from flask import Flask, Response
import pickle
import json


app = Flask(__name__)

model = pickle.load(open('Log_Reg_classification.pkl','rb'))

@app.route('/<int:sex>/<int:age>/<int:pulse>')
def index(sex, age, pulse):
    try:
        parameters = [[sex, age, pulse]]
        res = model.predict(parameters)[0]
        response_data = {
            'result': int(res)
        }
        json_response = json.dumps(response_data)
        return Response(json_response, content_type='application/json')
    except Exception as e:
        response_data = {
            'error': str(e)
        }
        json_response = json.dumps(response_data)
        return Response(json_response, content_type='application/json', status=500)

if __name__ == "__main__":
    app.run(debug=True)




