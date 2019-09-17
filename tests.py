import unittest
import requests

SERVER_URL = "http://localhost:5000"
RESERVATIONS = {}
for hour in ["10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm"]:
  RESERVATIONS[hour] = {
    "available": True,
    "player": None
  }

def test_index():
  response = requests.get(SERVER_URL + "/")

  assert response.status_code == 200
  assert response.text == "Welcome to tennis reservations"

def test_get_all_reservations():
   response = requests.get(SERVER_URL + "/reservations")

   assert response.status_code == 200, "Expected HTTP 200 status"
   assert response.json() == RESERVATIONS, "Expected JSON payload"

def test_get_one_reservation():
  response = requests.get(SERVER_URL + "/reservations?hour=11am")

  assert response.status_code == 200, "Expected HTTP 200 status"
  assert response.json() == RESERVATIONS['11am'], "Expected JSON payload for 11am"

def test_create_new_reservation():
  payload = {
    "hour": "11am",
    "player": "Jesse Wang"
  }
  response = requests.post(SERVER_URL + "/reservations", json=payload)

  assert response.status_code == 201, "Expected HTTP 201 status"
  assert response.json() == payload, "Expected JSON payload"
