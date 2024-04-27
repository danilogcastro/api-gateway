# Configurações

Para rodar este projeto, em conjunto com o projeto Rewards MVP, é necessário ter o Docker e Docker Compose instalado, bem como estar com ambos os projetos no mesmo diretório, criando um arquivo `docker-compose.yml` para poder orquestrar os containeres dos projetos e bases de dados.

O `docker-compose.yml` para orquestrar os projetos, bem como exemplos de arquivos de configurações necessários para rodá-los, mas que tipicamente ficam fora do controle de versão, podem ser encontrados [neste repositório](https://github.com/danilogcastro/configuration_files)

## Para fazer o build

```
docker compose build
```

### Para subir os projetos

```
docker compose up
```

Antes de tentar utilizar qualquer rota, é necessário criar as duas bases de dados:

```
docker compose exec db_gateway psql -U postgres
```

ou

```
docker compose exec db_rewards psql -U postgres
```

Dentro do console do Postgres:

```
CREATE DATABASE api_gateway_development;
```

```
CREATE DATABASE rewards_mvp_development;
```

E então rodar:

```
docker compose run rewards flask db upgrade
docker compose run api-gateway flask db upgrade
```
