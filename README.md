# Talana Kombat challenge

Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

## Main dependencies

This app was coded in Python using the following dependencies:

- Django
- djangorestframework
- pytest
- pylint

## Run the project

> Run all commands on the root folder

- Build app image

```bash
docker compose build
```

- Run app container

```bash
docker compose up -d
```

- View app logs

```bash
docker logs -f talana_app
```

- Run unit tests

```bash
docker exec -it talana_app pytest -v
```

## Fight API

### Endpoint

```bash
POST http://127.0.0.1:8000/api/fights
```

### Request

Use one of the following structures as a json request

```json
{
    "player1": {
        "movimientos": ["D", "DSD", "S", "DSD", "SD"],
        "golpes": ["K", "P", "", "K", "P"]
    },
    "player2": {
        "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
        "golpes": ["K", "", "K", "P", "P"]
    }
}
```

```json
{
    "player1": {
        "movimientos": ["SDD", "DSD", "SA", "DSD"],
        "golpes": ["K", "P", "K", "P"]
    },
    "player2": {
        "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
        "golpes": ["P", "K", "K", "K", "P", "K"]
    }
}
```

```json
{
    "player1": {
        "movimientos": ["DSD", "S"],
        "golpes": ["P", ""]
    },
    "player2": {
        "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
        "golpes": ["P", "", "P", "K", "K", "K"]
    }
}
```

### Postman example

![alt postman](screenshot.png)

### cURL example

```bash
curl --request POST 'http://127.0.0.1:8000/api/fights' \
--header 'Content-Type: application/json' \
--data-raw '{
    "player1": {
        "movimientos": ["D", "DSD", "S", "DSD", "SD"],
        "golpes": ["K", "P", "", "K", "P"]
    },
    "player2": {
        "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
        "golpes": ["K", "", "K", "P", "P"]
    }
}
'
```

### Response

```json
[
    "Tonyn se mueve y lanza una Patada",
    "Arnaldor lanza un Remuyuken",
    "Tonyn lanza un Taladoken",
    "Arnaldor se mueve",
    "Tonyn se mueve",
    "Arnaldor lanza un Remuyuken",
    "Arnaldor Gana la pelea y aun le queda 2 de energía"
]
```
