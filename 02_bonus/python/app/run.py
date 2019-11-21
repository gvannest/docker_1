''' Quick Fibonacci API '''

from flask import Flask
import json
import fib

app = Flask(__name__)

@app.route("/<number>", methods=['GET'])
def get_fib(number):
    ''' Return Fibonacci JSON '''
    return json.dumps(fib.get(int(number))), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
