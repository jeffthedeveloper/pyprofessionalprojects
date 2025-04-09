2. Estrutura do Projeto:

cafe_website/
├── app.py
├── cafes.db
├── templates/
│   ├── index.html
│   ├── add_cafe.html
│   └── edit_cafe.html
├── static/
│   ├── style.css
│   └── script.js


3. app.py (Backend com Flask):

4. templates/index.html (Página Principal):


5. templates/add_cafe.html e templates/edit_cafe.html (Formulários):

Crie formulários HTML semelhantes para adicionar e editar cafés, usando tags <form>, <input>, e <label>.

6. static/style.css (Estilos):

Adicione estilos CSS para melhorar a aparência do site.

7. Execução:

Execute app.py para iniciar o servidor Flask.

Reflexão:

Como abordei o projeto:
Planejei a estrutura do projeto e as rotas do Flask.
Implementei as funções do backend para interagir com o banco de dados.
Criei os templates HTML para a interface do site.
Adicionei estilos CSS para melhorar a aparência.
O que foi fácil:
A conexão com o banco de dados SQLite foi relativamente simples.
Criar as rotas básicas do Flask também foi direto.
O que foi difícil:
Implementar a lógica para editar e deletar cafés exigiu um pouco mais de atenção.
Garantir que a interface fosse responsiva e fácil de usar exigiu alguns ajustes.
Como posso melhorar para o próximo projeto:
Adicionar autenticação de usuário para proteger as funções de edição e exclusão.
Implementar uma função de pesquisa para encontrar cafés por nome ou localização.
Adicionar mapas para mostrar a localização dos cafés.
Melhorar a interface com um design mais moderno e responsivo.
Adicionar testes unitários.
Maior aprendizado:
A importância de separar o backend do frontend.
A importância de usar um framework web para facilitar o desenvolvimento.
A importância de planejar a estrutura do projeto antes de começar a codificar.
O que faria diferente:
Usaria um framework CSS como Bootstrap ou Tailwind para acelerar o desenvolvimento do frontend.
Implementaria testes unitários desde o início do projeto.
Usaria um ORM como SQLAlchemy para facilitar a interação com o banco de dados.