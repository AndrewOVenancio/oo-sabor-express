from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Drew', 10)
restaurante_praca.receber_avaliacao('lo', 8)
restaurante_praca.receber_avaliacao('Zen', 5)


def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()