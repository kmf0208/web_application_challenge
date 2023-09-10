from lib.album import Album


def test_construct_with_field():
    album = Album(1, 'Dark Side', 1995, 2)
    assert album.id == 1
    assert album.title == 'Dark Side'
    assert album.release_year == 1995
    assert album.artist_id == 2

def test_formatting():
    album = Album(1, 'Dark Side', 1995, 2)
    assert  album == Album(1, 'Dark Side', 1995, 2)


def test_album_are_equal():
    album1 = Album(1, "Test Artist", "Test Genre", 2)
    album2 = Album(1, "Test Artist", "Test Genre", 2)
    assert album1 == album2