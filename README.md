# Web Scraping com InfoMoney

Este projeto faz parte da disciplina de coleta e tratamento de dados do curso de Análise de Dados e Inteligência Artificial da UFMA. O objetivo é realizar a raspagem de dados, tratamento, normalização e transformação dos dados utilizando Python.

## 🚀 Objetivo do Projeto

O projeto visa:

- Raspar dados públicos do site **InfoMoney**, com foco nos dados de ações.
- Tratar os dados coletados (valores faltantes, ruídos e outliers).
- Normalizar e transformar os dados para melhor compreensão.
- Garantir que a raspagem respeite os Termos de Uso e o arquivo [`robots.txt`](https://www.infomoney.com.br/robots.txt/) do site.

---

## 🔍 Verificação Legal

### Política de privacidade

Com não ha termos de uso e somente as [política de privacidade](https://www.infomoney.com.br/politica-de-privacidade/) do site e não foi itentidicado nenhuma proibição do uso de Web Scraping.

### Robots.txt

O arquivo `robots.txt` do InfoMoney, disponível [aqui](https://www.infomoney.com.br/robots.txt/), não bloqueia o acesso às páginas públicas. Assim, a raspagem para fins acadêmicos está em conformidade.

---

## 📋 Pré-requisitos

Para executar o projeto, você precisa ter:

- Python 3.13.1 ou superior.
- Foram usadas as libs `requests`, `beautifulsoup4`, `pandas`, `numpy`, `matplotlib`, `selenium`, `streamlit` e `plotly`.

Instale os pacotes necessários com o comando:

```bash
pip install -r requirements.txt
```

---

## 🔧 Execução

### 1. Configuração

Clone este repositório e navegue até a pasta do projeto:

```bash
[git clone https://github.com/AbimaelAndrade/webscraping-infomoney.git](https://github.com/AbimaelAndrade/webscraping-infomoney.git)
cd webscraping-infomoney
```

### 2. Rodar o projeto

Execute o script realizar o scraping da página e mostrar os dados no dashboad.

```bash
streamlit run app.py
```

---

## 📖 Documentação

### Fontes de Dados

Os dados foram coletados da seção pública de Altas e Baixas das Ações da Bolsa do InfoMoney, acessível [aqui](https://www.infomoney.com.br/ferramentas/altas-e-baixas/).

### Métodos de Tratamento

- **Valores faltantes**: preenchidos com a média ou valores padrão.
- **Outliers**: identificados e removidos com base no método IQR.

---

## 🛠️ Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch: `git checkout -b sua-branch`.
3. Envie suas alterações: `git push origin sua-branch`.
4. Abra um pull request.

---

## 📝 Licença

Este projeto é destinado apenas para fins acadêmicos e segue os Termos de Uso do InfoMoney.

**Importante:** O uso dos dados deve respeitar as políticas de privacidade e direitos autorais do site.
