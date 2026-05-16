Adocao Pet
===========

Projeto Django para gerenciar a adoção de animais. Permite cadastro de usuários, pets, envio de múltiplas fotos por pet e o envio/gerenciamento de pedidos de adoção.

Como funciona
-------------

- Modelos principais:
	- `User`
	- `Pet`
	- `FotoPet`
	- `PedidoAdocao`
- Interface administrativa: painel do Django (`/admin`) com inlines para gerenciar
	fotos e pedidos diretamente no formulário do `Pet`.
- Uploads de imagens: arquivos enviados são salvos em `MEDIA_ROOT` (configurado
	em `adocao_pet/settings.py` como `media/`) e acessíveis via `MEDIA_URL`.

Como executar
--------------------------------

1. Criar e ativar um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências

```bash
pip install -r requirements.txt
```

3. Entrar no diretório do Django

```bash
cd adocao_pet
```

4. Aplicar migrações e criar superusuário

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Rodar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Rodando com Docker
------------------

1. Subir o backend e o banco PostgreSQL

```bash
docker compose up --build
```

2. Criar o superusuário no container

```bash
docker compose exec web python manage.py createsuperuser
```

3. Abrir o admin em

```text
http://localhost:8000/admin/
```

Observações
-----------

- O projeto usa `Pillow` para manipulação de imagens (necessário para
	`ImageField`).
