from flask import Flask  

meu_app = Flask (__name__) 

@meu_app.route('/')    
@meu_app.route('/rota1') 
def rota1():  
    return 'Olá, turma!'

@meu_app.route('/rota2')
def rota2():
    resposta = "<H3> Essa é outra página da rota 2 <H3>"
    return resposta
 
def saudacoes (nome): 
    return f'Olá, {nome}'

if __name__ == "__main__" :
    meu_app.run(port = 8000) 