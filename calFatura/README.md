# Projects
Projetos pessoais - (Modelo de Calculadora de Fatura de Energia)


Criado primeira versão de idei em excel Cal_Fat_Energia.xlsx, como modelo do código que seria utilizado.

A pois, foi criado um versão em Python dando início a aplicação em linguagem de programação, utilizando o calculo básico sobre a fatura de energia onde se pega a "Leitura Atual e subtrai pela "Leitura Anterior", dando assim o resultado de consumo em KWh. Em seguida mutiplicando pelo valor da tarifa e somando com a porcetagem do valor de iluminação pública e pins e confins caso tivesse.

Ressalto que o valor de Pis, Confins e Iluminação pública é apenas uma base da fatura que recebi, tendo em vista que essas informações precisas não obtive, sendo assim apenas um calculo sobre o valor de consumo da fatura.

Ex:       4220 (Leitura Atual)
-         4020 (Leitura Anterior)
=          200 (KWh)
*     0.834850 (Tarifa)
R$    166,97   (Valor em Real)

Onde o resultado final dará o valor em real como informado anteriormente "Valor de real em consumo de energia"