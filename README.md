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

Caso seja necessario fazer download do Dataset:

```bash
--download_dataset True
```

Caso o dataset esteja em outro diretório:

```bash
--dataset_path path
```

Caso seja necessario executar um prompt especifico:

```bash
--experiment True --prompt prompt1 'prompt 2'
```

OBS: caso o prompt tenha espaços entre a frase, utilize aspas simples ou aspas duplas

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