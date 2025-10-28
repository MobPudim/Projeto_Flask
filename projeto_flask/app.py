from flask import Flask, render_template

meu_app = Flask(__name__ , template_folder='templates')


@meu_app.route("/")  
def homepage():         
    return render_template ("homepage.html")

@meu_app.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__": 
     meu_app.run(port = 8000) 
                                