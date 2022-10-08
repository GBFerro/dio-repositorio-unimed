salario = int(input()) 

if (salario <= 600):
  novo_salario = salario*1.17
  reajuste = salario*0.17
  percentual = 0.17*100

elif (salario > 600) & (salario <= 900):
    
  novo_salario = salario*1.13
  reajuste = salario*0.13
  percentual = 0.13*100
  
elif (salario > 900) & (salario <= 1500):
  novo_salario = salario*1.12
  reajuste = salario*0.12
  percentual = 0.12*100
  
elif (salario > 1500) & (salario <= 2000):
  novo_salario = salario*1.1
  reajuste = salario*0.1
  percentual = 0.1*100

else: 
  novo_salario = salario*1.05
  reajuste = salario*0.05
  percentual = 0.05*100
  
print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual:.0f}%')

