# Espaço Múltimodal e engenharia de prompt
Segundo trabalho avaliativo da disciplina de Visão Computacional, ministrada pelo Prof. Dr. Cesar H. Comin

*Alunos:*
- Jayme Sakae dos Reis Furuyama ([jaymesakae](https://github.com/jaymesakae))
- Vitor Lopes Fabris ([tremefabris](https://github.com/tremefabris))
- Vinicius Gonçalves Perillo ([ViniciusPerillo](https://github.com/ViniciusPerillo))

## Como funciona

Para o melhor fluxo das inferencias, é recomendado seguir os seguintes comandos:

### Acúracia do Dataset
Executar o código de acuracia para todo o Datset

```bash
python3 main.py
```

### Com um prompt pré estabelecido
Executar o código usando um prompt especifico:

```bash
python3 main.py --experiment True --prompt 'dog' 'cat'
```

Podendo substituir cat e dog por qualquer prompt que seja necessário fazer um experimento.

### Parametros do código

Os parametros do código pode ser consultado com o seguinte comdando

```bash
python3 main.py -h
```


## Experimentos

Para os experimentos exigidos pela descrição do trabalho, é necessario rodar os seguintes comandos

```bash
python3 main.py --prompt "cat" "dog"
```

```bash
python3 main.py --prompt "A photo of a cat" "A photo of a dog"
```

```bash
python3 main.py --prompt "A photo of a cat, a type of pet" "A photo of a dog, a type of pet"
```