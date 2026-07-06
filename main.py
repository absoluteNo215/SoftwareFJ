from system import ManagementSystem
from ui import SoftwareFJApp

if __name__ == "__main__":
    app = SoftwareFJApp()
    app.mainloop()

def line():

    print("-" * 60)


system = ManagementSystem()


#clients
#interaction
line()
print("creating clients")
line()

try:

    system.add_client(
        "Jose Delgado",
        "123456",
        "josed@email.com",
        "3001234567"
    )

    system.add_client(
        "Maria Lopez",
        "654321",
        "maria@email.com",
        "3012223333"
    )

except Exception as error:

    print(error)


#duplicate client
line()
print("duplicate client")
line()

try:

    system.add_client(
        "idontknow",
        "123456",
        "test@email.com",
        "12345"
    )

except Exception as error:

    print(error)


#invalid email
line()
print("invalid email")
line()

try:

    system.add_client(
        "Carlos",
        "555555",
        "invalid_email",
        "123456"
    )

except Exception as error:

    print(error)


#service
line()
print("creating services")
line()

room = system.add_room_service(

    "Meeting room",

    15,

    80

)

equipment = system.add_equipment_service(

    "Projector",

    5,

    35

)

consulting = system.add_consulting_service(

    "Juan Perez",

    "Software dev",

    120

)


#valid reservation
line()
print("valid reservation")
line()

try:

    reservation = system.create_reservation(

        "123456",

        room.entity_id,

        4

    )

    print(reservation.get_info())

except Exception as error:

    print(error)


#invalid hours
line()
print("invalid hours")
line()

try:

    system.create_reservation(

        "123456",

        room.entity_id,

        -5

    )

except Exception as error:

    print(error)


#client not found
line()
print("client not found")
line()

try:

    system.create_reservation(

        "999999",

        room.entity_id,

        2

    )

except Exception as error:

    print(error)


#invalid service
line()
print("service not found")
line()

try:

    system.create_reservation(

        "123456",

        100,

        2

    )

except Exception as error:

    print(error)


#cancel reservation
line()
print("cancel reservation")
line()

try:

    system.cancel_reservation(1)

    print(system.search_reservation(1).status)

except Exception as error:

    print(error)


#confirm again
line()
print("confirm reservation")
line()

try:

    system.confirm_reservation(1)

    print(system.search_reservation(1).status)

except Exception as error:

    print(error)


#show data
line()
print("clients")
line()

system.show_clients()

line()
print("services")
line()

system.show_services()

line()
print("reservations")
line()

system.show_reservations()