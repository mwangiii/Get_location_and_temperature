from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from city import get_location
from Ip import get_ip
from weather import get_weather

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home_page():
    heading = "Check out!"
    lasting = "It's working"
    return heading + "https://njekev65.pythonanywhere.com/api/hello?visitor_name=%22Mark%22" + lasting

@app.route("/api")
def api_route():
    return "Hey you!"

class hello_visitor(Resource):
    def get(self):
        # visitor_name from query parameters
        visitor_name = request.args.get('visitor_name', 'Guest')
        # client's IP address
        client_ip = get_ip(request)
        location = get_location(client_ip)
        city = str(location)
        temperature = get_weather(city)

        # response in JSON
        response = {
            "client_ip": client_ip,
            "location": city,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
        }
        return jsonify(response)

api.add_resource(hello_visitor, "/api/hello")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
