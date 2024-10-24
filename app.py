# * import libraries
from flask import Flask, request
from function import createRDV, getDispo


app = Flask(__name__)


@app.route('/appointment/busy', methods=['GET', 'POST'])
def busy():
    # get body request
    data = request.json

    return {
        "results": [
            {
                "toolCallId": data['message']['toolCalls'][0]['id'],
                "result": str(getDispo())
            }
        ]
    }


@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    # get body request
    tempo_data = request.json

    # get info on appointment
    data = {}
    data['name'] = tempo_data['message']['toolCalls'][0]['function']['arguments']['name']
    data['summary'] = tempo_data['message']['toolCalls'][0]['function']['arguments']['bookingName']
    data['start'] = tempo_data['message']['toolCalls'][0]['function']['arguments']['bookingDateAndTime']
    data['end'] = tempo_data['message']['toolCalls'][0]['function']['arguments']['bookingEndDateAndTime']
    data['email'] = tempo_data['message']['toolCalls'][0]['function']['arguments']['email']
    data['phone'] = tempo_data['message']['toolCalls'][0]['function']['arguments']['phone']

    # create appointment
    error = createRDV(data)

    return {
        "results": [
            {
                "toolCallId": tempo_data['message']['toolCalls'][0]['id'],
                "result": error
            }
        ]
    }


if __name__ == '__main__':
    app.run()