import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Interacao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "somelink.com",
        "title": "Hotel"
    }

    link_repository.registry_link(link_infos)


@pytest.mark.skip(reason="Interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    links = link_repository.find_links_from_trip(link_id)
    #print(f'\n\nTrip_id: {trip_id}\n')
    assert isinstance(links, list)
    assert isinstance(links, tuple)
    print(links)

'''
@pytest.mark.skip(reason="Interacao com o banco")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)
'''


