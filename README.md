# Detecção e Análise de Desperdício de Alimentos no RU com YOLOv8 

Este repositório contém o pipeline automatizado para o treinamento de um modelo de visão computacional voltado à análise e quantificação de desperdício de alimentos no Restaurante Universitário (RU). 

O projeto utiliza a arquitetura **YOLOv8** e integra a API do **Roboflow** para o download dinâmico do dataset, aplicando técnicas avançadas de *Data Augmentation* e otimização de hiperparâmetros para garantir um modelo robusto e preciso.

---

##  Como Clonar e Configurar o Repositório

Siga os passos abaixo para baixar o projeto para a sua máquina e preparar o ambiente virtual. As instruções abaixo são focadas no uso com terminais Windows (PowerShell/CMD).

### 1. Clonar o repositório
Abra o seu terminal e execute o comando do Git para baixar os arquivos:
```bash
git clone https://github.com/filipesousa01/analise-desperdicio.git
````
###Entre na pasta do projeto recém-baixado:
````bash
cd analise-desperdicio
`````

### 2. Criar e ativar o ambiente virtual (Recomendado)

Para evitar conflitos com outras instalações do Python na sua máquina, crie um ambiente isolado:

````Bash
python -m venv venv
````
Ative o ambiente virtual (no PowerShell):

````Bash
.\venv\Scripts\Activate.ps1
````
(Você saberá que funcionou quando aparecer (venv) no início da linha do seu terminal).

### 3. Instalar as dependências

Com o ambiente ativado, instale as bibliotecas necessárias para processar a rede neural e baixar os dados:

````Bash
pip install ultralytics roboflow
````
