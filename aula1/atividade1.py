from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def texto():
    return '1. O que é um Decorator?Em Python, as funções são tratadas como objetos de primeira classe, o que permite que elas sejam enviadas como parâmetros para outras funções, como se fossem variáveis comuns. Um decorator é, na essência, uma função que "embrulha" outra função. Ele recebe a função original, injeta um comportamento extra ou modifica sua execução, e a entrega de volta pronta para ser executada. Visualmente, ele é identificado pelo símbolo @ (o famoso "açúcar sintático") colocado imediatamente acima da definição da função.' 

if __name__ == '__main__':
    app.run(debug=True)