from flask import Flask, render_template

meu_app = Flask(__name__)
 

@meu_app.route("/")  
def homepage():    
    return render_template ("homepage.html")

@meu_app.route("/index")
def indice():
    return render_template ("index.html") 

@meu_app.route("/contato")
def contato():
    return render_template("contato.html") 

@meu_app.route("/usuario")
def dados_usuario():
 
    dados_usu = {"nome": "Mariela","profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html",  dados = dados_usu)

@meu_app.route('/usuario/<id>')
def saudacao(id):
 
    return render_template('homepage_nome.html', nome=id)

@meu_app.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>") 

def usuario (nome_usuario, nome_profissao, nome_disciplina):
    
    dados_usu = {"profissao": nome_profissao, "disciplina": nome_disciplina}


    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)  

if __name__ == "__main__": 
     meu_app.run(port = 8000) 