from flask import Flask, render_template
from flask import request 
from flask import jsonify 

meu_app = Flask(__name__, template_folder='t_templates') 

meu_app.config['SECRET_KEY'] = "palavra-secreta-IFRO"

@meu_app.route("/")      
@meu_app.route("/index")  
def indice():
    return render_template ("t_index.html") 

@meu_app.route("/contato")
def contato():
    return render_template("t_contato.html") 


@meu_app.route("/usuario/<nome_usuario>;<nome_profissao>")

@meu_app.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  


@meu_app.route("/login")
def login():
    return render_template("t_login_flash_js_cadastro.html") 

@meu_app.route('/teste', methods=['GET', 'POST'])
def test_route():
    if request.method == 'GET':
        return jsonify(message="Requisição GET recebida!"), 200
    elif request.method == 'POST':
        return jsonify(message="Requisição POST recebida!"), 200
    else:
        return jsonify(error="Método não permitido"), 405


@meu_app.route("/autenticar", methods=['GET','POST']) 
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

@meu_app.route("/novocadastro/<nome_usuario>" , methods=['POST'])
@meu_app.route("/novocadastro/", defaults={"nome_usuario":""} , methods=['POST'])
def cadastroUsuario(nome_usuario):
    nome_usuario = request.form.get('nome_usuario')
    return render_template("t_cadastro.html", nome_login = nome_usuario ) 


if __name__ == "__main__": 
     meu_app.run(port = 8000) 
     
     