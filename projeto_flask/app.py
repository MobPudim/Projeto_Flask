from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, template_folder='t_templates')
app.secret_key = "segredo"

# ---------------- LOGIN ----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Exemplo simples (sem banco de dados)
        if email == "admin@ifro.edu.br" and senha == "123456":
            session['usuario'] = email
            flash("Login realizado com sucesso!")
            return redirect(url_for('usuario'))
        else:
            flash("Email ou senha inválidos.")
            return redirect(url_for('login'))

    return render_template('t_login.html')


# ---------------- CADASTRO ----------------
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        senha = request.form['senha']
        confirma = request.form['confirma']

        if senha != confirma:
            flash("As senhas não conferem! Tente novamente.")
            return redirect(url_for('cadastro'))

        flash("✅ Cadastro realizado com sucesso!")
        return redirect(url_for('login'))

    return render_template('t_login_flash_js_cadastro.html')


# ---------------- PÁGINA DO USUÁRIO ----------------
@app.route('/usuario')
def usuario():
    if 'usuario' not in session:
        flash("Você precisa estar logado para acessar esta página.")
        return redirect(url_for('login'))
    return render_template('t_usuario.html')


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash("Você saiu da conta.")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
