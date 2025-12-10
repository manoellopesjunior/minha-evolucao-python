import random
import time

# Dicionário com emojis
emojis = {"pedra": "✊", "papel": "✋", "tesoura": "✌️"}

# Placar
vitorias = 0
derrotas = 0
empates = 0

print("🎮=== JOKENPÔ ===🎮")

while True:
    print("\nFaça sua escolha:")
    print("pedra ✊  |  papel ✋  |  tesoura ✌️")

    escolha = input("👉 Sua escolha: ").lower()

    if escolha not in emojis:
        print("⚠️ Opção inválida! Tente novamente.")
        continue

    computador = random.choice(list(emojis.keys()))

    # Efeito dramático 😄
    print("\nJO...")
    time.sleep(0.5)
    print("KEN...")
    time.sleep(0.5)
    print("PÔ!!!\n")
    time.sleep(0.3)

    print(f"🧍 Você: {escolha} {emojis[escolha]}")
    print(f"💻 Computador: {computador} {emojis[computador]}\n")

    # Verifica resultado
    if escolha == computador:
        print("🤝 Empate!")
        empates += 1
    elif (escolha == "pedra" and computador == "tesoura") or \
         (escolha == "papel" and computador == "pedra") or \
         (escolha == "tesoura" and computador == "papel"):
        print("🎉 Você venceu!")
        vitorias += 1
    else:
        print("😢 Você perdeu!")
        derrotas += 1

    # Mostra o placar
    print(f"\n📊 Placar: {vitorias} Vitórias | {empates} Empates | {derrotas} Derrotas")

    # Pergunta se quer continuar
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("\n👋 Obrigado por jogar! Até a próxima!")
        break
