<h1>📚 Projeto de API de Teste com FastAPI</h1>

<p>Este projeto é uma API simples construída usando <a href="https://fastapi.tiangolo.com/">FastAPI</a>, um framework moderno e de alto desempenho para construir APIs em Python. O objetivo deste projeto é demonstrar como criar, configurar e testar uma API básica com FastAPI.</p>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li><strong>Rota de Boas-Vindas</strong>: Uma rota simples que retorna uma mensagem de boas-vindas.</li>
  <li><strong>Rota para Obter Dados de Restaurantes</strong>: Faz uma requisição para uma API externa que retorna dados de restaurantes e permite filtrar por nome de restaurante.</li>
</ul>

<h2>🛠 Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Python 3.7+</strong></li>
  <li><strong>FastAPI</strong></li>
  <li><strong>Uvicorn</strong> (Servidor ASGI para rodar a aplicação)</li>
  <li><strong>Requests</strong> (Biblioteca para fazer requisições HTTP)</li>
</ul>

<h2>📦 Estrutura do Projeto</h2>
<pre>
├── main.py          # Arquivo principal da aplicação
├── requirements.txt # Dependências do projeto
└── README.md        # Documentação do projeto
</pre>

<h2>🚧 Como Executar o Projeto</h2>

<h3>Pré-requisitos</h3>
<ul>
  <li>Certifique-se de ter o Python 3.7 ou superior instalado.</li>
  <li>É recomendável usar um ambiente virtual para evitar conflitos de dependências.</li>
</ul>

<h3>Passo a Passo</h3>
<ol>
  <li><strong>Clone este repositório:</strong>
    <pre><code>git clone https://github.com/CassAssump/basoc-api-Fastapi/
cd /basoc-api-Fastapi</code></pre>
  </li>

  <li><strong>Crie e ative um ambiente virtual (opcional, mas recomendado):</strong>
    <pre><code>python3 -m venv venv
source venv/bin/activate   # Para Linux/MacOS
venv\Scripts\activate      # Para Windows</code></pre>
  </li>

  <li><strong>Instale as dependências:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Execute a aplicação:</strong>
    <pre><code>uvicorn main:app --reload</code></pre>
  </li>

  <li><strong>Acesse a API:</strong>
    <ul>
      <li>Rota principal (boas-vindas): <code>http://127.0.0.1:8000/api/hello</code></li>
      <li>Rota para obter dados de restaurantes: <code>http://127.0.0.1:8000/api/restaurante?restaurante=NomeDoRestaurante</code></li>
    </ul>
  </li>

  <li><strong>Documentação da API:</strong>
    <ul>
      <li>Acesse a documentação interativa gerada automaticamente pelo FastAPI:</li>
      <li><strong>Swagger UI</strong>: <code>http://127.0.0.1:8000/docs</code></li>
      <li><strong>ReDoc</strong>: <code>http://127.0.0.1:8000/redoc</code></li>
    </ul>
  </li>
</ol>

<h2>📝 Exemplos de Uso</h2>

<h3>Rota de Boas-Vindas</h3>
<ul>
  <li><strong>Requisição:</strong>
    <pre><code>GET /api/hello</code></pre>
  </li>
  <li><strong>Resposta:</strong>
    <pre><code>{
  "message": "Hello World"
}</code></pre>
  </li>
</ul>

<h3>Rota de Restaurante</h3>
<ul>
  <li><strong>Requisição sem filtro:</strong>
    <pre><code>GET /api/restaurante</code></pre>
  </li>
  <li><strong>Requisição com filtro por nome de restaurante:</strong>
    <pre><code>GET /api/restaurante?restaurante=NomeDoRestaurante</code></pre>
  </li>
  <li><strong>Resposta:</strong>
    <pre><code>{
  "Restaurante": "NomeDoRestaurante",
  "Cardapio": [
    {
      "item": "Nome do Prato",
      "price": 12.99,
      "description": "Descrição do prato"
    }
  ]
}</code></pre>
  </li>
</ul>
