from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo - Davi Ferreira</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    background-color: #f4f7f6;
                    color: #333;
                    margin: 0;
                    padding: 40px;
                    display: flex;
                    justify-content: center;
                }
                .container {
                    background: #fff;
                    max-width: 700px;
                    width: 100%;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                    text-align: center;
                }
                h2 {
                    color: #2980b9;
                    margin-top: 25px;
                    font-size: 1.4rem;
                }
                ul {
                    list-style: none;
                    padding: 0;
                }
                li {
                    margin-bottom: 10px;
                    padding: 8px 12px;
                    background: #f9f9f9;
                    border-left: 4px solid #3498db;
                    border-radius: 4px;
                }
                strong {
                    color: #2c3e50;
                }
                .periodo {
                    float: right;
                    font-size: 0.9rem;
                    color: #7f8c8d;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Currículo Profissional</h1>

                <h2>Informações Pessoais</h2>
                <ul>
                    <li><strong>Nome:</strong> Davi Ferreira</li>  
                    <li><strong>Email:</strong> 22402187@aluno.cotemig.com.br</li>
                    <li><strong>Telefone:</strong> (31) 99526-2217</li>
                </ul>

                <h2>Experiência Profissional</h2>
                <ul>
                    <li>
                        <strong>Empresa:</strong> Minas Tênis <br>
                        <strong>Cargo:</strong> Jovem Aprendiz ADM 
                        <span class="periodo">Mar 2025 - Nov 2025</span>
                    </li>
                </ul>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
