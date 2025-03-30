# Scraper de Farmácias - Automatização de Coleta de Dados

Este projeto é uma solução automatizada para a coleta diária de dados de farmácias da minha cidade. Desenvolvido em Python, ele monitora informações de vendas por delivery, organiza os dados em arquivos CSV e os consolida em um único arquivo. O sistema utiliza APIs para obter dados de categorias e itens de farmácias específicas, garantindo um monitoramento eficiente e estruturado.

Os dados não serão mantidos no repositório por questões legais e termos de uso das plataformas acessadas.

## 🚀 Funcionalidades

- 📦 Coleta dados de farmácias a partir de portas de APIs expostas e raspagem de dados com Selenium.
- 📊 Organiza os dados em arquivos CSV separados por categoria e farmácia.
- 🔄 Consolida todos os arquivos CSV em um único arquivo para análise.
- ⚠️ Trata erros comuns, como falhas na requisição, problemas de decodificação JSON e campos ausentes.

## 📁 Estrutura do Projeto

```
📂 scraper_farmacias
├── 📄 main.py  # Arquivo principal que executa o scraper
├── 📂 scripts
│   ├── 📄 categories.py  # Função GetCategories para obter categorias disponíveis
│   ├── 📄 farmacias.py  # Função getFarmacias para listar farmácias
│   ├── 📄 transform.py  # Função transform_save_csv para salvar os dados em CSV
│   ├── 📄 consolidate.py  # Função GatherFiles para consolidar arquivos CSV
├── 📄 .env  # Arquivo para armazenar variáveis de ambiente
```

## ⚙️ Como Funciona o Algoritmo

1. **Inicialização**
   - O script carrega as variáveis de ambiente do arquivo `.env`.
   - A função `ExecuteScrapper` é chamada para iniciar o processo.

2. **Coleta de Dados**
   - A função `getFarmacias` retorna uma lista de farmácias.
   - Para cada farmácia, a função `GetCategories` retorna as categorias disponíveis.
   - Para cada categoria, o script faz uma requisição à API para obter os itens.

3. **Processamento e Armazenamento**
   - Os dados retornados pela API são processados e salvos em arquivos CSV, organizados por farmácia e categoria.
   - Os arquivos CSV são armazenados em pastas com o nome da farmácia.

4. **Consolidação**
   - Após a coleta de dados, a função `GatherFiles` consolida todos os arquivos CSV em um único arquivo para facilitar a análise.

5. **Tratamento de Erros**
   - O algoritmo trata erros de requisição, decodificação JSON, campos ausentes e outros erros inesperados, garantindo maior robustez.

## 📂 Estrutura de Saída

- **📁 Pastas por farmácia**: Cada farmácia terá uma pasta com arquivos CSV organizados por categoria.
- **📄 Arquivo consolidado**: Um único arquivo CSV contendo todos os dados coletados.

## ⏳ Automatização
- **⏰ Execução automática**: O programa é agendado no Windows por meio do aplicativo de Agenda de Tarefas, sendo disparado diariamente em um horário determinado para atualizar os dados de forma autônoma.

## 🛠️ Tecnologias Utilizadas

- Python 🐍
- Selenium 🌐
- Pandas 📊
- Requests 🔄
- dotenv 🔐


