from flask import Flask, jsonify, request
 
app = Flask (__name__)

@app.route('/')
def home ():
    return '<center><h1><hr>Aula criação de API</h1></center>'

@app.route('/api')
def demo():
   return jsonify(mensagem= "esta mensagem vai transformar a ")

@app.route('/api/<cliente>', methods=['GET'])
def nome(cliente):
   return jsonify(mensagem2=f'Olá{cliente}')

@app.route('/bemvindo/<idioma>/<nome>', methods=['get'])
def bemvindo(idioma, nome):
    mensagens = {
    'Inglês': 'Good morning',
    'Espanhol': 'Buenos días',
    'Francês': 'Bonjour',
    'italiano': 'Buongiorno',
    'Alemão': 'Guten Morgen'
    }

pedidos = [
   
     {'id':1,'cliente': 'heloisa','prato':'churrasco', 'status': 'aguardando'},
     {'id':2, 'cliente': 'Fabio', 'prato':'pizza', 'status':'aguardando'},

]

proximo_id = 3

@app.route('/pedidos', methods=['post'])
def novospedidos():
    global proximo_id
    novo_pedido = request.json

    novo_pedido_molde = {
       'id': proximo_id,
       'cliente': novo_pedido['cliente'],
       'prato': novo_pedido ['prato'],
       'status':'aguardando'

    }

    pedidos.append(novo_pedido_molde)
    proximo_id +=1
    return jsonify(novo_pedido_molde)

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify(pedidos)

    mensagens = mensagens.get(idioma)
    return jsonify(msg=f'{mensagens} {nome}')
if __name__ == '__main__':
  app.run(debug= True)