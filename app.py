from flask import Flask, request

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
 
def hel():
    return 'HELLO WORLD'

if __name__=='__main__':
    app.run(debug=True)