from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot('bob', tagger_language=ENGSM)

trainer = ListTrainer(chatbot)

trainer.train([
    'ola',
    'ola sou o bob,em que posso ajudar ?',
    'oi',
    'ola sou o bob,em que posso ajudar ?',
    'como faço o primeiro login no laboratorio ?',
    'o usuário é a sua matricula do cesupa, e a senha é sua data de nascimento dd/mm/aa, em que mais posso ajudar?',
    'como fazer o primeiro login no laboratorio ?',
    'o usuário é a sua matricula do cesupa, e a senha é sua data de nascimento dd/mm/aa, posso ajudar em mais alguma coisa ?',
    'onde fica a sala 1 ?',
    'fica no primeiro andar. posso ajudar em mais alguma coisa ?',
    'onde fica a sala 3 ?',
    'fica no segundo andar. posso ajudar em mais alguma coisa ?',
    'como são os computadores dos laboratorios ?',
    'são computadores capacitados,com bom desempenho,e equipados com varios programas e linguagens de programação pra voce treinar seus conhecimentos. mais alguma coisa ?',
     ])

while True:
    request = input('voce: ')
    response = chatbot.get_response(request)
    print('bob: ', response)

 