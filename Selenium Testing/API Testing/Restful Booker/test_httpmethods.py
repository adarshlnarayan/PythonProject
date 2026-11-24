import requests
import pytest

baseurl = "https://restful-booker.herokuapp.com/booking"


@pytest.mark.order(1)
@pytest.mark.dependency()
def test_createbooking():
    head = {'Content-Type': 'application/json'}
    payload = {
    "firstname" : "Adarsh",
    "lastname" : "narayan",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(f"{baseurl}", json = payload, headers = head)
    print(response.status_code)
    global booking_id
    booking_id = response.json()["bookingid"]
    print(booking_id)


@pytest.mark.order(2)
@pytest.mark.dependency(depends =["test_createbooking"])
def test_getbooking():
    head = {'Content-Type': 'application/json'}
    response = requests.get(f"{baseurl}/{booking_id}", headers = head)
    print(response.status_code)
    print(response.json())


@pytest.mark.order(3)
@pytest.mark.dependency(depends =["test_createbooking"])
def test_updatebooking():
    head = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }
    payload = {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.put(f"{baseurl}/{booking_id}", json = payload, headers = head)
    print(response.status_code)
    print(response.json())


@pytest.mark.order(4)
@pytest.mark.dependency(depends =["test_createbooking"])
def test_partialupdate():
    head = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }
    payload = {
    "firstname" : "Adarsh",
    "lastname" : "Narayan"
}
    response = requests.patch(f"{baseurl}/{booking_id}", json = payload, headers = head)
    print(response.status_code)
    print(response.json())


@pytest.mark.order(5)
@pytest.mark.dependency(depends =["test_createbooking"])
def test_deletebooking():
    head = {'Content-Type': 'application/json'}
    response = requests.delete(f"{baseurl}/{booking_id}", headers = head)
    print(response.status_code)
