# Scraper de Farmácias

Este projeto é um scraper desenvolvido em Python para coletar dados de farmácias da minha cidade diariamente mantendo monitoramento de informações de vendas delivery, organizá-los em arquivos CSV e consolidá-los em um único arquivo. Ele utiliza APIs para obter informações de categorias e itens de farmácias específicas.

Os dados não serão mantidos no repositório por questões legais e termos de uso das plataformas acessadas

## Funcionalidades

- Coleta dados de farmácias a partir de portas de API's expostas e raspagem de dados com selenium.
- Organiza os dados em arquivos CSV separados por categoria e farmácia.
- Consolida todos os arquivos CSV em um único arquivo para análise.
- Trata erros comuns, como falhas na requisição, problemas de decodificação JSON e campos ausentes.

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que executa o scraper.
- **`scripts/categories.py`**: Contém a função `GetCategories`, que retorna as categorias disponíveis para uma farmácia.
- **`scripts/farmacias.py`**: Contém a função `getFarmacias`, que retorna a lista de farmácias a serem processadas.
- **`scripts/transform.py`**: Contém a função `transform_save_csv`, que transforma os dados e os salva em arquivos CSV.
- **`scripts/consolidate.py`**: Contém a função `GatherFiles`, que consolida todos os arquivos CSV gerados em um único arquivo.
- **`.env`**: Arquivo de configuração para armazenar variáveis de ambiente, como a URL base da API.

## Como Funciona o Algoritmo

1. **Inicialização**:
   - O script carrega as variáveis de ambiente do arquivo `.env`.
   - A função `ExecuteScrapper` é chamada para iniciar o processo.

2. **Coleta de Dados**:
   - A função `getFarmacias` retorna uma lista de farmácias.
   - Para cada farmácia, a função `GetCategories` retorna as categorias disponíveis.
   - Para cada categoria, o script faz uma requisição à API para obter os itens.

3. **Processamento e Armazenamento**:
   - Os dados retornados pela API são processados e salvos em arquivos CSV, organizados por farmácia e categoria.
   - Os arquivos CSV são armazenados em pastas com o nome da farmácia.

4. **Consolidação**:
   - Após a coleta de dados, a função `GatherFiles` consolida todos os arquivos CSV em um único arquivo para facilitar a análise.

5. **Tratamento de Erros**:
   - O algoritmo trata erros de requisição, decodificação JSON, campos ausentes e outros erros inesperados, garantindo maior robustez.

## Estrutura de Saída

- **Pastas por farmácia**: Cada farmácia terá uma pasta com arquivos CSV organizados por categoria.
- **Arquivo consolidado**: Um único arquivo CSV contendo todos os dados coletados.

## Automatização
- **Programa do sistema windows**: Através do aplicativo de agenda de tarefas, o algoritimo é atualizado todo dia em um horario determinado.
