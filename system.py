from models.client import Client
from models.reservation import Reservation
from models.room_service import RoomService
from models.equipment_service import EquipmentService
from models.consulting_service import ConsultingService
from utils.logger import Logger
from utils.exceptions import *



class ManagementSystem:

    def __init__(self):

        self.clients = []
        self.services = []
        self.reservations = []

        self.next_client_id = 1
        self.next_service_id = 1
        self.next_reservation_id = 1

    #clients
    def add_client(self, name, document, email, phone):

        for client in self.clients:

            if client.document == str(document):
                raise DuplicateClientError(
                    "client already exists"
                )

        client = Client(
            self.next_client_id,
            name,
            document,
            email,
            phone
        )

        self.clients.append(client)

        Logger.info(f"client {client.name} created.")

        self.next_client_id += 1

        return client

    def get_clients(self):

        return self.clients

    def search_client(self, document):

        for client in self.clients:

            if client.document == str(document):
                return client

        return None

    def remove_client(self, document):

        client = self.search_client(document)

        if client is None:
            raise InvalidClientError("client not found")

        self.clients.remove(client)

        Logger.warning(
            f"Client {client.name} removed."
        )

    #service
    def add_room_service(
            self,
            room_name,
            capacity,
            hourly_rate):

        service = RoomService(

            self.next_service_id,

            room_name,

            capacity,

            hourly_rate

        )

        self.services.append(service)

        self.next_service_id += 1

        Logger.info(
            f"room service {room_name} created"
        )

        return service

    def add_equipment_service(
            self,
            equipment_name,
            stock,
            daily_rate):

        service = EquipmentService(

            self.next_service_id,

            equipment_name,

            stock,

            daily_rate

        )

        self.services.append(service)

        self.next_service_id += 1

        Logger.info(
            f"equipment service {equipment_name} created"
        )

        return service

    def add_consulting_service(
            self,
            consultant,
            specialty,
            hourly_rate):

        service = ConsultingService(

            self.next_service_id,

            consultant,

            specialty,

            hourly_rate

        )

        self.services.append(service)

        self.next_service_id += 1

        Logger.info(
            f"consulting service {consultant} created"
        )

        return service

    def get_services(self):

        return self.services

    def search_service(self, service_id):

        for service in self.services:

            if service.entity_id == service_id:
                return service

        return None

    def remove_service(self, service_id):

        service = self.search_service(service_id)

        if service is None:
            raise InvalidServiceError(
                "service not found"
            )

        self.services.remove(service)

        Logger.warning(
            f"service {service.name} removed"
        )

    #reservations
    def create_reservation(

            self,

            client_document,

            service_id,

            hours):

        client = self.search_client(client_document)

        if client is None:
            raise InvalidClientError(
                "client not found"
            )

        service = self.search_service(service_id)

        if service is None:
            raise InvalidServiceError(
                "service not found"
            )

        reservation = Reservation(

            self.next_reservation_id,

            client,

            service,

            hours

        )

        reservation.process()

        self.reservations.append(reservation)

        self.next_reservation_id += 1

        Logger.info(
            f"reservation {reservation.reservation_id} created"
        )

        return reservation

    def get_reservations(self):

        return self.reservations

    def search_reservation(self, reservation_id):

        for reservation in self.reservations:

            if reservation.reservation_id == reservation_id:
                return reservation

        return None

    def cancel_reservation(self, reservation_id):

        reservation = self.search_reservation(
            reservation_id
        )

        if reservation is None:
            raise InvalidReservationError(
                "reservation not found"
            )

        reservation.cancel()

    def confirm_reservation(self, reservation_id):

        reservation = self.search_reservation(
            reservation_id
        )

        if reservation is None:
            raise InvalidReservationError(
                "reservation not found"
            )

        reservation.confirm()

    #show
    def show_clients(self):

        for client in self.clients:

            print(client)

    def show_services(self):

        for service in self.services:

            print(service)

    def show_reservations(self):

        for reservation in self.reservations:

            print(reservation)