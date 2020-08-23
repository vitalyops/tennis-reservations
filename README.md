## Tennis reservations

A simple web server where users can reserve an hourly time slot to play tennis on a single tennis court. This tennis court is open every day from 10am to 10pm which gives tennis players 12 hours of play time each day.

### API

Uses [Flask](http://flask.pocoo.org/) Python web framework. Serve employs a REST API and responds to HTTP requests.

### `GET /`

Prints a simple welcome message `Welcome to tennis reservations`.


### `GET /reservations`

List all hourly time slots. If `available` is set to `true` it means that time slot is available and `player` will contain a name of a player that made that reservation.

##### Successful Response

```json
{
  "10am": {
    "available": true,
    "player": null
  },
  "11am": {
    "available": false,
    "player": "Jesse Wang"
  },
  "12pm": {
    "available": true,
    "player": null
  },
  ...
}
```

##### Possible Errors

 - `500 "Internal Server Error"`


### `GET /reservations?hour=11am`

Fetch reservation for specific hour. URL query parameter `hour` should be in the flollowing format `HHam` or `HHpm`.

##### Successful Response

```json
{
  "available": false,
  "player": "Jesse Wang"
}
```

##### Possible Errors

 - `400 "Invalid hour format"`
 - `500 "Internal Server Error"`


### `POST /reservations`

Player can make a reservation **only** if that `hour` is available.

#### Request Body

```json
{
  "hour": "11am",
  "player": "Jesse Wang"
}
```

#### Successful Response

`200 OK`	
`201 Created`

#### Possible Errors

 - `400 "Invalid body"`
 - `400 "Invalid 'hour' parameter"`
 - `400 "Invalid 'player' parameter"`
 - `409 "Reservation for '11am' already exists"`
 - `500 "Internal Server Error"`


### Running

Use `flask` command to start the server

```console
python server.py
```

### Testing

1. Make sure you have the server running
2. Install `pip install requests nose` and then run

```console
nosetests -d
```
