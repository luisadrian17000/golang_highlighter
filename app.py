#"""
# 
# 
# 
# """

from flask import Flask, request, jsonify, render_template
import ply.lex as lex
import golang_rules

app = Flask(__name__)

colors = {
    "ID" : "#979196",
    "DIGIT" : "#FF0000",
    "FUNCTION" : "#CECB18",
    "OPERANDS" : "#FF33F0",
    "STR" : "#E07515",
    "CARRIAGERETURN" : "",
    "SPACE" : ""
    }

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
        
        if tok.type == "CARRIAGERETURN":
            processed_text += f'<span style="color: {colors[tok.type]};">{tok.value}</span><br>'
        else:
            processed_text += f'<span style="color: {colors[tok.type]};">{tok.value}</span>'

    # Devolver el texto procesado
    return jsonify({'html': processed_text})

if __name__ == '__main__':
    app.run(debug=True)
