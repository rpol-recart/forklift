def test_get_forklifts(client):
    response = client.get('/api/forklifts')
    assert response.status_code == 200


def test_post_forklift(client):
    data = {"name": "New Forklift", "type": "Heavy Duty"}
    response = client.post('/api/forklifts', json=data)
    assert response.status_code == 201
