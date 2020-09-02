from chatterbot import ChatBot , filters
from chatterbot.trainers import ListTrainer
import os
import re

class MeuChatBot(ChatBot):

    def tratar_dados(self):
        regex1 = r'\<.+\>\s|^\d+\n.+$\n.+\>|\-.+\-|\d+\:\d+\:\d+\,\d+\s\-\-\>\s\d+\:\d+\:\d+\,\d+|^\d+\s'
        regex2 = r'^\s\s\s'
        regex3 = r'^\s\-\s|^\-\s'
        regex4 = r'^\s'
        regex5 = r'$\n(?=[a-z]+)'
        substituir1 = ''
        substituir2 = ' '
        diretorio = os.path.expanduser('~/Documents/Chatbot/Legendas/')
        
        for legenda in os.listdir(diretorio):
            if legenda.endswith(".txt"):
                abrir = open(diretorio+legenda, 'r')
                fonte = abrir.read()
                resultado = re.sub(regex1, substituir1, fonte, 0, re.MULTILINE)
                resultado = re.sub(regex2, substituir1, resultado, 0, re.MULTILINE)
                resultado = re.sub(regex3, substituir1, resultado, 0, re.MULTILINE)
                resultado = re.sub(regex4, substituir1, resultado, 0, re.MULTILINE)
                resultado = re.sub(regex5, substituir2, resultado, 0, re.MULTILINE)
                abrir.close()
                #abrir = open(diretorio+legenda, 'w')
                abrir = open('treino.txt', 'a')
                abrir.write(resultado)

    def treina(self):
        diretorio = os.path.expanduser('~/Documents/Chatbot/Legendas/')
        self.trainer = ListTrainer(self)
        abrir = open('treino.txt', 'r')
        fonte = abrir.readlines()
        self.trainer.train(fonte)
        #for legenda in os.listdir(diretorio):
        #    if legenda.endswith(".txt"):
        #        abrir = open(diretorio+legenda, 'r')
        #        fonte = abrir.readlines()
        #        self.trainer.train(fonte)
                
