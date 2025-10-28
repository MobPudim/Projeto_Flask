from flask import Flask, render_template
from flask import request 
from flask import jsonify 

app_Mariela = Flask(__name__, template_folder='t_templates') 

app_Mariela.config['SECRET_KEY'] = "palavra-secreta-IFRO"

@app_Mariela.route("/")      
@app_Mariela.route("/index")  
def indice():
    return render_template ("t_index.html") 

@app_Mariela.route("/contato")
def contato():
    return render_template("t_contato.html") 


@app_Mariela.route("/usuario/<nome_usuario>;<nome_profissao>")

@app_Mariela.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  


@app_Mariela.route("/login")
def login():
    return render_template("t_login_flash_js_cadastro.html") 

@app_Mariela.route('/teste', methods=['GET', 'POST'])
def test_route():
    if request.method == 'GET':
        return jsonify(message="Requisição GET recebida!"), 200
    elif request.method == 'POST':
        return jsonify(message="Requisição POST recebida!"), 200
    else:
        return jsonify(error="Método não permitido"), 405


@app_Mariela.route("/autenticar", methods=['GET','POST']) 
def autenticar_api():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if verificar_login(usuario, senha):
        return jsonify({"status": True, "mensagem": "Login bem-sucedido"})
    else:
        return jsonify({"status": False, 
                        "mensagem": "Login ou senha incorretos",
                        "user": usuario,
                        "pwd": senha }), 401
    

tabelaUsuarios = {
    "mariela": "SuperSenh@2000",
    "alunoIFRO": "SuperSenh@2010",
    "visitante": "SuperSenh@2020"
}


def verificar_login(login, senha):
    if login in tabelaUsuarios and tabelaUsuarios[login] == senha:
        return True
    else:
        return False

@app_Mariela.route("/novocadastro/<nome_usuario>" , methods=['POST'])
@app_Mariela.route("/novocadastro/", defaults={"nome_usuario":""} , methods=['POST'])
def cadastroUsuario(nome_usuario):
    nome_usuario = request.form.get('nome_usuario')
    return render_template("t_cadastro.html", nome_login = nome_usuario ) 


if __name__ == "__main__": 
     app_Mariela.run(port = 8000) 
     
     