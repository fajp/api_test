import requests
import apimap


data_ = {
    "firstname" : "Jim",
    "lastname" : "Neutron",
    "totalprice" : 111,
    "depositpaid" : 'true',
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
data_2 = {
    "firstname" : "Jim",
    "lastname" : "TEST!",
    "totalprice" : 111,
    "depositpaid" : 'true',
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

api = apimap.ApiMap()
id = api.create_booking(data_)
print(api.get_booking(id))
api.update_booking(id, data_2)
print(api.get_booking(id))
print(id)
api.delete_booking(id)
print(api.get_booking(id))
