"""
Tests restful-booker API
https://restful-booker.herokuapp.com

Tests:
    - getting token
    - getting booking ids
    - getting booking info by id
    - creating booking
    - updating booking
    - partialy updating booking
    - delete booking
"""

import apimap


TEST_CREATE = {
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

TEST_UPDATE = {
    "firstname" : "Filip",
    "lastname" : "Piechnik",
    "totalprice" : 200,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2022-04-01",
        "checkout" : "2022-04-03"
    },
    "additionalneeds" : "Pyszny obiadek"
}

TEST_PART_UPDATE = {
    "totalprice" : 0,
    "depositpaid" : True,
}

try:
    api = apimap.ApiMap()
    print('Create session and getting token: OK')
except:
    print('Create session and getting token: ERROR')

try:
    id = api.get_booking_ids()[0]
    print(f'Get id: OK ({id})')
except:
    print('Get id: ERROR')

try:
    api.get_booking(id)
    print(f'Get booking by id: OK')
    print(f' ->{api.get_booking(id)}')
except:
    print('Get booking by id: ERROR')

try:
    api.update_booking(id, TEST_UPDATE)
    print(f'Update booking: OK')
    print(f' ->{api.get_booking(id)}')
except:
    print(f'Update booking: ERROR')

try:
    api.partial_update_booking(id, TEST_PART_UPDATE)
    print(f'Partial update booking: OK')
    print(f' ->{api.get_booking(id)}')
except:
    print('Partial update booking: ERROR')

try:
    api.delete_booking(id)
    if id not in api.get_booking_ids():
        print(f'Delete booking: OK')
except:
    print('Delete booking: ERROR')
