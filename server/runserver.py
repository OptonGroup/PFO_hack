"""
Flask Server for Data Prediction

This script sets up a Flask server that provides predictions based on location data.
It uses a pre-trained model to make predictions and returns the results as JSON.

Dependencies:
- Flask
- flask_cors
- functions (custom module)
- model (custom module)
- webbrowser

The server exposes one endpoint:
- /data/<location>: Returns prediction data of companies for the specified location

Usage:
Run this script to start the Flask server. It will automatically open a web browser
to http://127.0.0.1:5000/index.html when the server starts.

Note: Ensure all dependencies are installed and the custom modules (functions and model)
are in the same directory as this script.
"""



from flask import Flask
from flask import jsonify
import functions
import model
import webbrowser
from flask_cors import CORS

print('Идёт подргузка данных... Ожидайте')
app = Flask(__name__, static_url_path='')
CORS(app)
infos = functions.main()
md = model.Model()

def get_data_from_model(location):
    """
    Retrieve and process prediction data of companies for a given location.

    Args:
        location (str): The location to get predictions for.

    Returns:
        list: A list of dictionaries containing prediction results, including:
            - ID: The identifier of the prediction
            - Company: The size of the company (e.g., 'Крупный бизнес')
            - Score: The prediction score

    The function filters data based on the given location, makes predictions using
    the pre-loaded model, and returns the top 20 results
    """
    to_predict = []
    inds_predict = []
    for n_id in infos:
        if infos[n_id]['Location'] == location:
            to_predict.append(infos[n_id])
            inds_predict.append(n_id)
            
    predict = md.get_ans(to_predict)
    ans = []
    for i in range(len(predict)):
        if predict[i] < 95:
            ans.append([inds_predict[i], predict[i]])
    ans.sort(key=lambda x: int(x[1]),reverse=True)
    json_ans = []
    company = {
        4: 'Крупный бизнес',
        3: 'Средний бизнес',
        2: 'Малый бизнес',
        1: 'Микро бизнес'
    }
    for i in range(min(20, len(ans))):
        json_ans.append({
            "ID": ans[i][0],
            "Company": company[infos[ans[i][0]]['B']],
            "Score": ans[i][1]
        })
    return json_ans

@app.route('/data/<location>')
def data(location):
    """
    Flask route that returns prediction data for a given location.

    Args:
        location (str): The location to get predictions for.

    Returns:
        flask.Response: A JSON response containing the prediction data.
    """
    return jsonify(get_data_from_model(location=location))

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/index.html')
    app.run()