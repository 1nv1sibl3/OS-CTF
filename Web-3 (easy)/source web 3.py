from flask import Flask, request, Response

app = Flask(__name__)

# Flag to be retrieved using the HEAD method
FLAG = "OSCTF{Und3Rr47Ed_H3aD_M3Th0D}"

# Home page route
@app.route('/')
def index():
    return "Welcome to my first ever website."

# Route to retrieve the flag using HEAD method
@app.route('/get-flag', methods=['HEAD'])
def get_flag():
    if request.method == 'HEAD':
        response = Response()
        response.headers['Flag'] = FLAG
        return response


if __name__ == '__main__':
    app.run(debug=True)
