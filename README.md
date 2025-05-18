# 🧠 Sistema Multi-Agente para Consultas em Banco de Dados (DuckDB)

Este projeto é um sistema **multi-agente inteligente** desenvolvido dentro da **[Formação Arquiteto de IA** da DascIA](https://lp.dascia.com.br/lcfaiafev25-matricula-pg1?utm_source=org&utm_medium=github&utm_campaign=PPDASCIAFAIA&utm_term=text2sql)**.  
Na formação, mergulhamos fundo em **inteligência artificial aplicada**, com foco em **sistemas autônomos**, **orquestração de agentes**, **RAG**, **LLM Routing**, **automação com IA**, entre outros tópicos avançados do universo da IA moderna.

## 📌 O que é esse projeto?

Este é um sistema multi-agente que permite que o usuário escreva uma **pergunta em linguagem natural**, e receba:
1. A **query SQL equivalente**, adaptada para DuckDB;
2. O **resultado da consulta formatado** para leitura humana (markdown);
3. Uma **resposta amigável em linguagem natural**, como se fosse um atendente de WhatsApp.

Tudo isso é feito por agentes separados e especializados, que cooperam entre si para entender a pergunta, consultar o banco e retornar a melhor resposta possível.

## ⚙️ Componentes do sistema

- **SQLAgent**: transforma linguagem natural em SQL (especificamente DuckDB).
- **CheckerAgent**: verifica se a query é segura (sem DELETE, UPDATE etc.).
- **Executor**: executa a consulta no banco local.
- **Formatter**: transforma o resultado do DataFrame em markdown.
- **Responder**: gera uma resposta natural e informal com base no resultado.

## 📚 Tecnologias e ferramentas

- Python 3.11+
- DuckDB
- Langchain / Pydantic
- Pandas
- Arquitetura multi-agente

## ▶️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPO]
   cd [NOME_DA_PASTA]
   ```
2. Instale as dependências com Poetry:
   ```bash
   poetry install
   ```
3. Ative o ambiente virtual do Poetry:
   ```bash
   eval $(poetry env activate)
   ```
4. Execute toda a aplicação (lembre-se de ter configurado o .env com sua chave API da OpenAI):
   ```bash
   python src/main.py
   ```

## 📎 Formação Arquiteto de IA
Este projeto é apenas uma das aplicações ensinadas na Formação Arquiteto de IA, onde você aprende a construir sistemas de IA que realmente funcionam no mundo real, com foco em produtização, automação e monetização de soluções com IA.

👉 [Clique aqui para conhecer a formação](https://lp.dascia.com.br/lcfaiafev25-matricula-pg1?utm_source=org&utm_medium=github&utm_campaign=PPDASCIAFAIA&utm_term=text2sql)