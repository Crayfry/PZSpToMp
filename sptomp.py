import sqlite3
try:
    mpDbConn = sqlite3.connect('players.db')
    spDbConn = sqlite3.connect('1players.db')
    mpCur = mpDbConn.cursor()
    spCur = spDbConn.cursor()
except Exception as err:
    print("something went wrong with database connections " + str(err))
try:
    characterNum = input("Type the character id")
    spCur.execute("""SELECT x, y, data from localPlayers WHERE id=?""", [characterNum])
    resultList = spCur.fetchall()
    xCoor = resultList[0][0]
    yCoor = resultList[0][1]
    data = resultList[0][2]
    userName = input("Type your user name")
    mpCur.execute("""UPDATE networkPlayers SET x=?, y=?, data=? WHERE username=?""", [xCoor,yCoor,data,userName])
    mpDbConn.commit()
except Exception as err:
    print("something went wrong with data manipulation " + str(err))
finally:
    mpCur.close()
    spCur.close()
    mpDbConn.close()
    spDbConn.close()