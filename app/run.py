import flask as flk

app = flk.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    # save user input in query
    query = flk.request.args.get('query')

    return flk.render_template(
        'index.html',
        query=query,
        samples=[]
    )

def main():
    app.run(host='0.0.0.0', port=3001, debug=True)

if __name__ == '__main__':
    main()