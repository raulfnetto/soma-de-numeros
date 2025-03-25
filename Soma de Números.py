def main():

    numeros = input("Digite uma série de números, e separe-os por espaço, nós vamos lhe mostrar a soma deles: ").strip()

    numeros = numeros.split(" ")

    numeros_int = [int(num) for num in numeros]

    soma = sum(numeros_int)

    print(f"\nA soma dos seus números é: {soma}\n\n")

def menu():

        print("\nPressione: '1' se você quer começar!\nPressione: '2' se você quer sair!")

        opcao = input()
        
        if opcao == '1':
            main()
            menu()
        
        if opcao == '2':
            exit()

        else:
            print("Opção inválida! ❌")
            menu()


menu()
