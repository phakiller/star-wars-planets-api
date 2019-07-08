# Star Wars Planets - API

O intuito desta API é gerenciar os planetas para a franquia de filmes [Star Wars](https://www.starwars.com).

### Tecnologias Utilizadas

* [**Python**](https://www.python.org)
  * [**Sanic**](https://sanic.readthedocs.io/en/latest/)
  * [**Sanic Restful**](https://github.com/CoCongV/sanic-restful)
  * [**Sanic Motor**](https://github.com/lixxu/sanic-motor)
  * [**Sanic Cors**](https://github.com/ashleysommer/sanic-cors)
  * [**Marshmallow**](https://marshmallow.readthedocs.io/en/3.0/index.html)
  * [**Marshmallow Dataclass**](https://lovasoa.github.io/marshmallow_dataclass/html/marshmallow_dataclass.html)
  * [**aiohttp**](https://aiohttp.readthedocs.io/en/stable/)
* [**MongoDB**](https://www.mongodb.com)

* [**Docker**](https://www.docker.com)

* [**Docker Compose**](https://docs.docker.com/compose/)

* [**Swagger UI**](https://swagger.io/tools/swagger-ui/)



### Rodando a aplicação

#### Requisitos

* Docker

* Docker Compose

Para rodar a aplicação basta executar o comando:

```sh
make go
```

Depois de tudo *startado* os Endpoints ficarão disponivel em:

* Aplicação: [localhost:6606](http://0.0.0.0:6606)
* Documentação: [localhost:6607](http://0.0.0.0:6607)

A interação com a API pode ser feita por meio da documentação, onde será exibida uma tela como a abaixo, onde você poderá ver as repostas dos Endpoints bem como os parâmetros que podem ser passados:

![Swagger Home](/images/swagger_homescreen.png "Swagger Home")