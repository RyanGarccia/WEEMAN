#
# misc.py - usefull functions
#
# This file if part of weeman project
#
# See 'LICENSE' file for copying
#


import sys
import time

# help options
help_options = {"url" : "O URL da pagina da Web, com https:// or http://.",
                "action_url" : "O URL de acao de forma da pagina.",
                "port" : "A porta Weeman vai ouvir",
                "user_agent" : "Weeman User-Agent string.",
                "html_file" : "Permite que voce carregue o arquivo HTML em vez de URL.",
                "external_js" : "Permite que voce inclua um script externo para ser carregado.",
                "set" : "Define um valor para a opcao, set <option> <value>.",
                "run" : "Executa o servidor, alias = \'r\'.",
                "clear" : "Limpa a tela.",
                "help" : "Todos nos sabemos... (:",
                "quit" : "quit, alias = \'q\'."}


def printt(s, msg):
    
    if s == 1:
        print("\033[01;31mErro: %s\033[00m")
        sys.exit(1)
    elif s == 2:
        print("[%s]\033[01;32m %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    elif s == 3:
        print("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    else:
        print("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))

def print_help():

    print("\t\033[01;32m")
    print("\tshow        : exibe as opcoes.")
    print("\tset         : seleciona acao (set <option> <value>)")
    print("\trun         : inicia o server.")
    print("\tclear       : limpa a tela.")
    print("\thelp        : exibe a ajuda (help <opcao>.)")
    print("\tframework   : Removido Nesta Versao...")
    print("\tquit        : quit.\033[00m")

def print_help_option(option):

    found = 0
    for opt in help_options.items():
        if opt[0] == option:
            found = 1
            printt(32, "%s - %s" %(option, opt[1]))
    if not found:
        printt(3, "Erro: Opcao \'%s\' nao encontrada." %option)

def isroot():

    if os.getuid() !=0:
        printt(1,"Execute o Weeman como ROOT.")
