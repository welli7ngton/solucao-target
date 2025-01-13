def main(k, indice, soma=0):
    if k >= indice:
        return soma
    return main(k + 1, indice, soma + (k + 1))


if __name__ == '__main__':
    print(main(0, 13))
