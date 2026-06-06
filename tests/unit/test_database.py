from database import db

def test_database_connection_opens_successfully():
    db.connect(reuse_if_open=True)
    assert not db.is_closed()
    db.close()

    