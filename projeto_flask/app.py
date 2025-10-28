from flask import Flask, render_template

meu_app = Flask(__name__, template_folder='t_templates') 

@meu_app.route("/")      
@meu_app.route("/index")  
def indice():
    return render_template ("t_index.html") 

@meu_app.route("/contato")
def contato():
    return render_template("t_contato.html") 

@meu_app.route("/login")
def login():
    return render_template("t_login.html") 

@meu_app.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""}) 
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

if __name__ == "__main__": 
     meu_app.run(port = 8000) 
     