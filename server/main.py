from flask import Flask, render_template, request, jsonify
import util
import os
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    template = os.listdir('../ui')
    print(template)
    context = {}
    return render_template('../ui/app.html', context)
@app.route('/classify_image', methods= ['GET','POST'])
def classify_image():
    image_data = request.form['image_data']
    back_response = util.classify_image(image_data)
    response = jsonify(back_response)
    print(back_response)
    response.headers.add('Access-control-Allow-Origin','*')

    return response
if __name__== "__main__":
    print("Starting Python Flask Server")
    util.load_saved_artifacts()
    app.run(port=5000)