
while True: 
    try: 
        perna = input()
        lingua = ['ingles', 'frances', 'portugues', 'caiu']
        
        if perna == 'esquerda':
          print(lingua[0])
        
        if perna == 'direita':
          print(lingua[1])
        
        if perna == 'nenhuma':
          print(lingua[2])
        
        if perna == 'ambas':
          print(lingua[3])
        
    except EOFError: 
        break
        