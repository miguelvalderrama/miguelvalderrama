import flask
from flask.json import jsonify

app = flask.Flask(__name__)



@app.route("/")
def index():
    #Just render template
    return flask.render_template("layout.html")

@app.route("/vige", methods=['POST'])
def vige():
    #Check and store values
    message = flask.request.form.get('message')
    key = flask.request.form.get('key')
    met = flask.request.form.get('met')

    #Sanity checks
    #Check if the message was submitted and is alpha chars
    if not message:
        return jsonify({'error': 'Missing Message!'})
    elif not message.isalpha():
        return jsonify({'error': 'Only alphabetics characters!'})

    #Check if the key was submitted and is alpha chars
    elif not key:
        return jsonify({'error': 'Missing Key!'})
    elif not key.isalpha():
        return jsonify({'error': 'Only alphabetics characters!'})

    keyword = generate_key(message, key)

    #Check if the user wants to decodify or encrypt
    if met == 'encrypt':
        cipher = encrypt(message, keyword)
    elif met == 'decrypt':
        cipher = decrypt(message, keyword)

    return jsonify({'success': cipher})

def generate_key(message, key):
    key = list(key)
    #Compare key length with the message length
    if len(key) == len(message):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
    
def encrypt(message, key):
    encrypt = []
    for i in range(len(message)):
        x = (ord(message[i].upper()) + ord(key[i].upper())) % 26
        x += ord('A')
        encrypt.append(chr(x))
    return("" . join(encrypt))

def decrypt(message, key):
    decrypt = []
    for i in range(len(message)):
        x = (ord(message[i].upper()) - ord(key[i].upper()) + 26) % 26
        x += ord('A')
        decrypt.append(chr(x))
    return("" .join(decrypt))

