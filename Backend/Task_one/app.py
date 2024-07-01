"""
a basic web server in flask stack.
expose an API endpoint that conforms to the criteria below:
Endpoint: [GET] <example.com>/api/hello?visitor_name="Mark"
(where <example.com> is your server origin)
Response:
{"client_ip": "127.0.0.1", // The IP address of the requester,
"location": "New York" // The city of the requester
"greeting": "Hello, Mark!, the temperature is 11 degrees Celcius in New York"
}
"""
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

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
        # Get the visitor_name from query parameters
        visitor_name = request.args.get('visitor_name', 'Guest')
        # Get the client's IP address
        client_ip = request.remote_addr
        location = "New York"
        temperature = 11

        # Construct the response JSON
        response = {
            "client_ip": client_ip,
            "location": location,
            "greeting": f"Hello, {visitor_name}!,the temperature is {temperature} degrees Celsius in {location}"
        }
        return jsonify(response)


api.add_resource(hello_visitor, "/api/hello")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
