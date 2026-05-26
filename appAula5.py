from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    usario1 = {
    "nome": "Theo",
    "senha": 22401130,
}
    usario2 = {
    "nome": "Janaina",
    "senha": "cotemig2026",
}
    usario3 = {
    "nome": "Dolga ",
    "senha": "cotemig2026",
}
    usario4 = {
    "nome": "antonio",
    "senha": "cotemig2026",
}

    if usuario == 'Theo' and senha == '22401130':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    elif usuario == 'Janaina' and senha == 'cotemig2026':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    elif usuario == 'Antonio' and senha == 'cotemig2026':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    elif usuario == 'Dolga' and senha == 'cotemig2026':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    else:
        return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)