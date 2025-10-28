from flask import Flask, render_template, request, redirect, url_for, flash

# Indica explicitamente que os templates estão dentro da pasta "t_templates"
app = Flask(__name__, template_folder='t_templates')
app.secret_key = "segredo"  # usada pelo flash()

# ---------------- ROTA DE LOGIN ----------------
@app.route('/')
def login():
    # Renderiza a tela de login
    return render_template('t_login.html')


# ---------------- ROTA DE CADASTRO ----------------
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        senha = request.form['senha']
        confirma = request.form['confirma']

        # Validação de senha
        if senha != confirma:
            flash("As senhas não conferem! Tente novamente.")
            return redirect(url_for('cadastro'))

        flash("✅ Cadastro realizado com sucesso!")
        return redirect(url_for('login'))

    # Renderiza o formulário de cadastro
    return render_template('t_login_flash_js_cadastro.html')


# ---------------- ROTA DE USUÁRIO ----------------
@app.route('/usuario')
def usuario():
    return render_template('t_usuario.html')


# ---------------- EXECUÇÃO ----------------
if __name__ == '__main__':
    app.run(debug=True)
