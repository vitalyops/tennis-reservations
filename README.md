# Tennis reservations

Build a simple web server where people can reserve an hourly time slot to play tennis on a single tennis court. This tennis court is open every day from 10am to 10pm which gives tennis players 12 hours of play time each day.

## Development

1. Clone the repository `git clone https://github.com/nilgradisnik/tennis-reservations.git`
2. Create a new branch `git checkout -b my-work`
3. Commit your changes `git add --all; git commit -a`
4. Push your changes `git push`
5. Create a pull request on github

## API

Use [Flask](http://flask.pocoo.org/) Python web framework. Server should implmement [REST API](http://www.restapitutorial.com/) which will respond to HTTP requests.

## `GET /`

Prints a simple welcome message `Welcome to tennis reservations`.


## `GET /reservations`

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


## `GET /reservations?hour=11am`

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


## `POST /reservations`

Create a new reservation. Player can make a reservation **only** if that `hour` is available.

#### Request Body

```json
{
  "hour": "11am",
  "player": "Jesse Wang"
}
```

#### Successful Response

`201 Created`

#### Possible Errors

 - `400 "Invalid body"`
 - `400 "Invalid 'hour' parameter"`
 - `400 "Invalid 'player' parameter"`
 - `409 "Reservation for '11am' already exists"`
 - `500 "Internal Server Error"`


## Running

Use `flask` command to start the server

```console
FLASK_APP=server.py flask run
```

## Testing

1. Make sure you have the server running
2. Install `pip install requests nose` and then run

```console
nosetests -d
```
