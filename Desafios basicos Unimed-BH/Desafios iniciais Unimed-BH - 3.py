tempo, velocidade_media = map(int,input().split())

consumo = 12
litros_gasolina = (velocidade_media * tempo) / consumo

print(f'{litros_gasolina:.3f}')
