import time
import sys

class SproutPulse:
    def __init__(self):
        self.pontos_energia = 0
        self.estagio_arvore = "🌱 Broto"
        self.historico_foco = []

    def atualizar_arvore(self):
        """Atualiza o estágio da árvore com base nos pontos acumulados"""
        if self.pontos_energia >= 30:
            self.estagio_arvore = "🌳 Carvalho Adulto"
        elif self.pontos_energia >= 15:
            self.estagio_arvore = "🌿 Arbusto Forte"
        else:
            self.estagio_arvore = "🌱 Broto"

    def rodar_cronometro(self, minutos, tarefa):
        """Executa a contagem regressiva do tempo de foco"""
        segundos = minutos * 60
        print(f"\n🔒 [MODO DEEP WORK ACTIVATED]")
        print(f"Focando em: '{tarefa}'")
        print(f"Status Atual: {self.estagio_arvore} ({self.pontos_energia} pts)\n")

        try:
            # Em um teste rápido, você pode mudar time.sleep(1) para time.sleep(0.01)
            while segundos > 0:
                mins, segs = divmod(segundos, 60)
                tempo_formatado = f"{mins:02d}:{segs:02d}"
                
                # Desenha uma barra de progresso simples no terminal
                sys.stdout.write(f"\r⏳ {tempo_formatado} | Cuidando do seu broto... Não feche o app!")
                sys.stdout.flush()
                
                time.sleep(1) 
                segundos -= 1

            # Sucesso
            self.pontos_energia += 10
            self.atualizar_arvore()
            self.historico_foco.append({"tarefa": tarefa, "duracao": minutos, "status": "Concluído"})
            
            print("\n\n🎉 CICLO CONCLUÍDO COM SUCESSO!")
            print(f"✨ +10 Pontos de Energia adicionados!")
            print(f"Nova evolução: Sua planta agora é um {self.estagio_arvore}!")
            print("\n☕ Hora de descansar 5 minutos. Beba uma água!")

        except KeyboardInterrupt:
            # Se o usuário tentar cancelar o programa (burlar o foco)
            print("\n\n❌ ALERTA: Você interrompeu o ciclo de foco!")
            print("🍂 Seu broto murchou um pouco... Nenhuns pontos foram ganhos.")
            self.historico_foco.append({"tarefa": tarefa, "duracao": minutos, "status": "Interrompido"})

    def iniciar(self):
        """Menu principal do aplicativo via terminal"""
        print("====== BEM-VINDO AO SPROUTPULSE ======")
        
        while True:
            print("\n1. Iniciar Novo Bloco de Foco (25 min)")
            print("2. Ver Status da Árvore")
            print("3. Sair do Aplicativo")
            
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                tarefa = input("O que você vai produzir agora? ")
                if not tarefa.strip():
                    tarefa = "Tarefa Geral"
                # Usaremos 25 minutos como padrão
                self.rodar_cronometro(25, tarefa)
            elif opcao == "2":
                print(f"\n--- 🌲 Seu Estado Atual ---")
                print(f"Estágio da Planta: {self.estagio_arvore}")
                print(f"Pontos de Energia Acumulados: {self.pontos_energia} XP")
            elif opcao == "3":
                print("\nObrigado por usar o SproutPulse! Até a próxima sessão de foco. 👋")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Executa o aplicativo
if __name__ == "__main__":
    app = SproutPulse()
    app.iniciar()
