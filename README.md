# Agente Nexus

Agente básico que consulta e recupera informações a partir de uma base de conhecimento da ENAP.

# Requisitos

Para executar esse projeto são necessários as seguintes ferramentas:

- **[Python](https://www.python.org/downloads/release/python-31213/) (3.12.13):** Linguagem de programação usada.
- **[uv]():** Gerenciador de dependências e ambientes virtuais.
- **[Docker](https://docs.docker.com/desktop/setup/install/linux/):** Usado para executar o Qdrant.
- **[Qdrant](https://qdrant.tech/):** Banco de dados vetorial.

# Execução

Primeiro precisamos criar nosso ambiente virtual e instalar as dependências:

```bash
uv sync
```

Agora precisamos baixar a imagem do qdrant para usarmos no docker:

```bash
docker pull qdrant/qdrant
```

E então precisamos executar nosso banco de dados vetorial localmente na porta 6333:

```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant
```

Por fim, podemos rodar o código do agente:

```bash
uv run python main.py
```

E para interagir com o agente via chat basta acessar o [link](os.agno.com).