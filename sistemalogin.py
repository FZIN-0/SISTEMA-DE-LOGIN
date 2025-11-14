import time
import sys
import getpass

# Funções para efeitos visuais/sons
def print_com_animacao(texto, delay=0.035):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def barra_de_loading(qtd_pontos=3, tempo=0.5):
    for _ in range(qtd_pontos):
        print(".", end='', flush=True)
        time.sleep(tempo)
    print("")

def cor(texto, cor):
    cores = {
        'azul': '\033[94m', 'verde': '\033[92m', 'amarelo': '\033[93m',
        'vermelho': '\033[91m', 'magenta': '\033[95m', 'reset': '\033[0m'
    }
    return f"{cores[cor]}{texto}{cores['reset']}"

# Dados de login
login_correto = "Fabricio"
senha_correta = "sukuna123"

print(cor("=== 🎓 BEM-VINDO AO SISTEMA DE LOGIN ESCOLAR ===", "azul"))
print_com_animacao("Você tem 3 tentativas para acertar o login e a senha.😅\n")

tentativas = 3

while tentativas > 0:
    login = input(cor("👤 Login: ", "azul"))
    senha = getpass.getpass(cor("🔒 Senha: ", "magenta"))  # senha 'invisível'

    if login == login_correto and senha == senha_correta:
        print()
        print(cor("✅ Login bem-sucedido! Bem-vindo(a), ", 'verde') + cor(login_correto + "!", 'amarelo'))
        print(cor("Carregando o sistema", 'magenta'), end="")
        barra_de_loading()
        time.sleep(0.6)
        print(cor("\n🌟=== PAINEL ESCOLAR INTERATIVO ===🌟", "amarelo"))
        print(cor("1️⃣  Ver suas notas", "verde"))
        print(cor("2️⃣  Consultar horário das aulas", "verde"))
        print(cor("3️⃣  Enviar mensagem ao professor", "verde"))
        print(cor("4️⃣  Jogar Batalha Naval da Escola 🛳️", "verde"))
        print(cor("5️⃣  Sair\n", "verde"))

        opcao = input(cor("▶️ Escolha uma opção (1-5): ", "amarelo"))

        if opcao == "1":
            print_com_animacao("\n📘 Suas notas: Matemática 9.5, Português 8.7, Ciências 10.0! Parabéns! 🏅", 0.04)
        elif opcao == "2":
            print_com_animacao("\n📅 Segunda a Sexta - 07:30 às 12:00", 0.04)
        elif opcao == "3":
            print_com_animacao("\n💬 Mensagem enviada com sucesso! O professor irá responder em breve. ✉️", 0.04)
        elif opcao == "4":
            print_com_animacao("\n🛳️ Modo Batalha Naval em desenvolvimento: aguarde surpresas! Mas já considere-se capitão do conhecimento! ⚓😃", 0.04)
        elif opcao == "5":
            print_com_animacao("\n👋 Saindo do sistema... Até logo. Volte sempre!", 0.04)
        else:
            print_com_animacao("\n❓ Opção misteriosa e secreta! (ou inválida 😆) Mas adorei sua curiosidade!", 0.04)
        break
    else:
        tentativas -= 1
        print(cor("❌ Login ou senha incorretos.", "vermelho"))
        if tentativas > 0:
            print_com_animacao(f"Você ainda tem {tentativas} tentativa(s). Respire fundo e tente novamente!\n", 0.04)
        else:
            print(cor("\n🚫 Suas tentativas acabaram! Acesso bloqueado por motivos de segurança escolares. ☹️", "vermelho"))

print_com_animacao(cor("=== Fim do programa ===", "magenta"),
