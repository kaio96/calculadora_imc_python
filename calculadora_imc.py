def main():

    def calculo(peso, altura):
        calculo = peso / altura ** 2
        return calculo

    def imc():
        imc = round(calculo(peso, altura), 1)

        if imc < 18.5:
            print('O seu imc é {} e você está abaixo do peso '.format(imc))
            opcoes()
        elif imc > 18.5 < 24.9:
            print('O seu imc é {} e você está com um peso normal '.format(imc))
            opcoes()
        elif imc > 25 < 29.9:
            print('O seu imc é {} e você está com excesso de peso '.format(imc))
            opcoes()
        elif imc > 30 < 34.1:
            print('O seu imc é {} e você está com obesidade classe 1 '.format(imc))
            opcoes()
        elif imc > 35 < 39.9:
            print('O seu imc é {} e você está com obesidade classe 2 '.format(imc))
            opcoes()
        elif imc > 25 < 29.9:
            print('O seu imc é {} e você está com obesidade classe 3 '.format(imc))
            opcoes()

    def opcoes():
        opcao = int(input("Tecle 1 para continuar ou 0 para encerrar: "))
        
        if opcao == 1:
            main()
        else:
            print("Encerrando aplicação...")


    peso = float(input('Informe o seu peso: '))
    altura = float(input('Informe a sua altura: '))

    imc()


main()
