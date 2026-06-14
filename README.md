# World Cup API 

A REST API built with Flask that provides historical FIFA World Cup data, including champions, top scorers, star players and host countries.

## Features

* List all World Cups
* Search a World Cup by edition year
* Historical tournament data
* RESTful endpoints
* JSON responses

## Technologies

* Python
* Flask
* JSON
* Render (Deployment)

## Endpoints

### Get all World Cups

```GET /world-cups```

### Get a specific World Cup

```GET /world-cups/<edition>```

**Example:**

```GET /world-cups/2002```

## Example Response

```json
{
    "edition": 2002,
    "host": "South Korea and Japan",
    "winner": "Brazil",
    "top_scorer": "Ronaldo",
    "star_players": ["Ronaldo", "Ronaldinho", "Rivaldo", "Cafu"]
}
```