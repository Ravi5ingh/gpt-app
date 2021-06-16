import flask as flk

app = flk.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    return flk.render_template('index.html')

def main():
    app.run(host='0.0.0.0', port=3001, debug=True)

if __name__ == '__main__':
    main()