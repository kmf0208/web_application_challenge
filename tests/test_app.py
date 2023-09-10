



def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
       "Album(1, The Cold Nose, 2008, 1)"



def test_post_lbums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post("/albums", data= {
        'title': 'In Ear Park',
        'release_year': '2008',
        'artist_id': '1'
    })
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
       "Album(1, The Cold Nose, 2008, 1)\n" \
       "Album(2, In Ear Park, 2008, 1)"
    

def test_post_albums_with_no_data(db_connection, web):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post("/albums")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "" \
       "you need submite titile , relase_year and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
       "Album(1, The Cold Nose, 2008, 1)"