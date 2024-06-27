from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <body>
                <h1>Search</h1>
                <form action="/search" method="get">
                    <input type="text" name="query">
                    <input type="submit" value="Search">
                </form>
            </body>
        </html>
    '''

@app.route('/search')
def search():
    query = request.args.get('query')
    # XSS vulnerability: directly reflecting user input in the response
    return f'''
        <html>
            <body>
                <h1>Search Results for: {query}</h1>
                <p>No results found.</p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
