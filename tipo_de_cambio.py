# -*- coding: utf-8 -*-

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    ammount = float(raw_input('ingresa la cantidad de pesos mexicanos que quieres convertir: '))

    result =  foreign_exchange_calculator(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 154.97
    return mex_to_col_rate * ammount

if __name__ == '__main__':
    run() 