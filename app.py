from flask import Flask, render_template, request
import requests
app = Flask(__name__)

#global varibale
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=28.633184,%2077.219385&radius=500&type=restaurant&keyword=McDonalds&key=AIzaSyA2VaWLZG0WlsRU6NMy9SQ2ce-NPVMFKgY'

#landing page
@app.route("/")
def index():
    return render_template('index.html')



#function to return json object from url
def getdict():
    r=requests.get(url)
    # Decode the JSON data into a dictionary: json_data
    json_data=r.json()
    return(json_data)

#dictionary object
def getinfo():
    dict=getdict()
    list=dict["results"]
    newlist=[]
    for x in list:
        y=x['vicinity']
        newlist.append(y)
    return(newlist)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form["search"]
      var=getinfo()
      return render_template("nearme.html", result = result, vars=var)


if __name__ == "__main__":
    app.debug=True
    app.run(host='127.0.0.1', port=5000 )
