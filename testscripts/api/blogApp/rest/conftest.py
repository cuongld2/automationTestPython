import pytest

from utilities.database import MySQL

mysql_drive = MySQL()


@pytest.fixture(scope='session')
def set_up_mysql():
    connection = mysql_drive.connect('localhost', 'restapi', 'root', 'cuong1990')
    yield connection
    mysql_drive.close(connection)




