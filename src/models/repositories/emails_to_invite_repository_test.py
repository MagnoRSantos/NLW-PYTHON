import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trip_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olamundo222@email.com"
    }

    emails_to_invite_repository.registry_email(email_trip_infos)


@pytest.mark.skip(reason="Interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    #print(f'\n\nTrip_id: {trip_id}\n')
    print(emails)

'''
@pytest.mark.skip(reason="Interacao com o banco")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)
'''


