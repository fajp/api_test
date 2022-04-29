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

final_result = True

try:
    api = apimap.ApiMap()
    print('Create session and getting token: OK')
except:
    print('Create session and getting token: ERROR')
    final_result = False

try:
    id = api.get_booking_ids()[0]
    print(f'Get id: OK ({id})')
except:
    print('Get id: ERROR')
    final_result = False

try:
    api.get_booking(id)
    print(f'Get booking by id: OK')
except:
    print('Get booking by id: ERROR')
    final_result = False

try:
    api.update_booking(id, TEST_UPDATE)

    comp_update = True
    for key in TEST_UPDATE.keys():
        if TEST_UPDATE[key] != api.get_booking(id)[key]:
            comp_update = False
    
    if comp_update:
        print(f'Update booking: OK')
    else:
        print(f'Update booking: ERROR')
        final_result = False
except:
    print(f'Update booking: ERROR')
    final_result = False

try:
    api.partial_update_booking(id, TEST_PART_UPDATE)

    comp_part_update = True
    for key in TEST_PART_UPDATE.keys():
        if TEST_UPDATE[key] != api.get_booking(id)[key]:
            comp_update = False
    
    if comp_part_update == True:
        print(f'Partial update booking: OK')
    else:
        print(f'Partial update booking: ERROR')
        final_result = False
except:
    print('Partial update booking: ERROR')
    final_result = False

try:
    api.delete_booking(id)
    if id not in api.get_booking_ids():
        print(f'Delete booking: OK')
except:
    print('Delete booking: ERROR')
    final_result = False

try:
    id_create = api.create_booking(TEST_CREATE)

    comp_create = True
    for key in TEST_CREATE.keys():
        if TEST_CREATE[key] != api.get_booking(id_create)[key]:
            comp_create = False
    
    if comp_create:
        print(f'Create booking: OK')
    else:
        print(f'Create booking: ERROR')
        final_result = False
except:
    print('Create booking: ERROR')
    final_result = False

if final_result:
    print('Final result: OK')
else:
    print('Final result: ERROR(s) occurred')
