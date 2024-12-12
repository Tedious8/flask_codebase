from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Set DEBUG to False for Production
DEBUG = True

# Set port to 5000 (port 5000 is usually use for backend)
PORT = 5000

# Every route need to use @app.route to define the path for specific URL followed by a function
# E.g., http://127.0.0.1:5000
@app.route('/')
def index():
    # If you go to 127.0.0.1:PORT and see this, it means the app is working
    return jsonify({
        'status': 200,
        'message': 'Success',
        'data': {}
    })

# If you go to 127.0.0.1:PORT/task_1?courseName=courseName and see this, it means this task is working
# E.g., http://127.0.0.1:5000/task_1?courseName=Statistic
@app.route('/task_1', methods=['GET'])
def task_1():
    # Get the parameter for courseName
    courseName = request.args.get('courseName')

    if courseName is None:
        return jsonify({
            'status': 400,
            'message': 'Bad request',
            'data': {}
        })

    '''
    TODO
    '''

    return jsonify({
        'status': 200,
        'message': 'Success',
        'data': {
            'courseName': courseName
        }
    })

# If you go to 127.0.0.1:PORT/task_2?schoolName=schoolName and see this, it means this task is working
# E.g., http://127.0.0.1:5000/task_2?schoolName=NTHU
@app.route('/task_2', methods=['GET'])
def task_2():
    # Get the parameter for schoolName
    schoolName = request.args.get('schoolName')

    if schoolName is None:
        return jsonify({
            'status': 400,
            'message': 'Bad request',
            'data': {}
        })

    '''
    TODO
    '''

    return jsonify({
        'status': 200,
        'message': 'Success',
        'data': {
            'schoolName': schoolName
        }
    })

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)