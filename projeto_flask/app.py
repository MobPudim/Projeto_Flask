from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, template_folder='t_templates')
app.secret_key = "segredo"

# ---------------- LOGIN ----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Login simples (sem banco de dados)
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
@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    return render_template('t_usuario.html')


# ---------------- VERIFICADOR DE NOME ----------------
@app.route('/verificar-nome', methods=['GET', 'POST'])
def verificar_nome():
    nome = None
    resultado = None

    if request.method == 'POST':
        nome = request.form['nome']
        resultado = f'O nome \"{nome}\" já existe no sistema!'

    return render_template('t_verificar_nome.html', nome=nome, resultado=resultado)


# ---------------- VERIFICADOR DE ALTURA ----------------
@app.route('/verificar-altura', methods=['GET', 'POST'])
def verificar_altura():
    altura = None
    resultado = None

    if request.method == 'POST':
        try:
            altura = float(request.form['altura'])
            if altura > 2.20:
                resultado = f'Tá mentindo, {altura:.2f}m é muita coisa!'
            else:
                resultado = f'Sua altura de {altura:.2f}m foi registrada com sucesso!'
        except ValueError:
            resultado = "Por favor, insira um número válido."

    return render_template('t_verificar_altura.html', altura=altura, resultado=resultado)


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash("Você saiu da conta.")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
