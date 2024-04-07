# import pytest
import os
os.environ["SQLITE_DB_DIR"] = os.path.dirname(os.path.abspath(__file__))
os.environ["SQLITE_DB_NAME"] = "test.db"

db_file = os.path.join(os.environ["SQLITE_DB_DIR"], os.environ["SQLITE_DB_NAME"])
if os.path.exists(db_file):
    os.remove(db_file)

from  fastapi.testclient import TestClient
from cloud_orbit_api.main import app
from cloud_orbit_api.db_factory import SQLiteSingleton

def test_read_item():
    client = TestClient(app)

    response = client.post("/items/", json={"name": "Item 1", "description": "Description 1"})
    assert response.status_code == 200

    # Test case for an existing item
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1", "description": "Description 1"}

    # Test case for a non-existing item
    response = client.get("/items/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
