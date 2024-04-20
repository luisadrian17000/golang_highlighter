# app.py
from flask import Flask, request, jsonify, render_template
import ply.lex as lex
import golang_rules

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    content = request.json
    text_to_lex = content['text']
    
    # Utilizar golang_rules para procesar el texto
    lexer = golang_rules.getLexer()
    lexer.input(text_to_lex)
    
    # Extraer los tokens y generar HTML
    processed_text = ''
    while True:
        tok = lexer.token()
        if not tok:
            break
        processed_text += f'<span style="color: #FFBF80;">{tok.value}</span>'

    # Devolver el texto procesado
    return jsonify({'html': processed_text})

if __name__ == '__main__':
    app.run(debug=True)
