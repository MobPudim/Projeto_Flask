from flask import Flask, render_template

meu_app = Flask(__name__ , template_folder='templates')


@meu_app.route("/")  
def homepage():         
    return render_template ("homepage.html")

@meu_app.route("/contato")
def contato():
    return render_template("contato.html") 

@meu_app.route("/index")
def indice():
    return render_template ("index.html") 

@meu_app.route("/usuario")
def dados_usuario():

    dados_usu = {"nome": "Neymar", "profissao": "Jogador", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados = dados_usu)

if __name__ == "__main__": 
     meu_app.run(port = 8000) 
                                