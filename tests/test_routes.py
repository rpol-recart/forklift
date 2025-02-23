import pytest
from run import server
from app.models import LoaderManager


@pytest.fixture
def client():
    """
    Create a Flask test client for testing the API.

    This fixture sets up the Flask application in testing mode,
    initializes a LoaderManager with two loaders, and attaches it to the app's context.
    It then yields the test client for use in tests.
    """
    server.config['TESTING'] = True
    loader_manager = LoaderManager()
    loader_manager.add_loader('loader_001')
    loader_manager.add_loader('loader_002')
    server.loader_manager = loader_manager
    with server.test_client() as c:
        yield c


def test_api_get_status(client):
    """
    Test the /api/get-forklift-status/<forklift_id> endpoint.

    This test checks the following:
    - The response status code is 200 (OK).
    - The JSON response contains the correct forklift ID.
    - The status field in the JSON response is None.
    - The raw response data matches the expected JSON string.

    Args:
        client: A Flask test client instance provided by the fixture.
    """
    response = client.get('/api/get-forklift-status/loader_001')
    print(response)
    decoded = response.get_json()
    assert response.status_code == 200
    assert decoded['forklift_id'] == 'loader_001'
    assert decoded['status'] is None
    assert decoded['name'] == 'KoneKranes'


def test_api_get_all(client):
    """
    Test the /api/get-all-forklifts endpoint.

    This test checks the following:
    - The response is not None.
    - The JSON response contains exactly two forklift entries.
    - The response status code is 200 (OK).
    - The first entry in the JSON response has the correct forklift ID and status.

    Args:
        client: A Flask test client instance provided by the fixture.
    """
    response = client.get('/api/get-all-forklifts')
    assert response is not None
    decoded = response.get_json()
    assert len(decoded) == 2
    assert response.status_code == 200
    assert decoded[0]['forklift_id'] == 'loader_001'
    assert decoded[0]['status'] == 'full'
