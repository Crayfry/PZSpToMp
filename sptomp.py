import sqlite3
try:
    singleplayer = input("insert the name of the singleplayer database (.db) file")
    multiplayer = input("insert the name of the multiplayer database (.db) file")
    mpDbConn = sqlite3.connect(multiplayer)
    spDbConn = sqlite3.connect(singleplayer)
    mpCur = mpDbConn.cursor()
    spCur = spDbConn.cursor()
except Exception as err:
    print("something went wrong with database connections " + str(err))
try:
    characterNum = input("Type the character id")
    spCur.execute("""SELECT name, x, y, z, data from localPlayers WHERE id=?""", [characterNum])
    resultList = spCur.fetchall()
    name = resultList[0][0]
    xCoor = resultList[0][1]
    yCoor = resultList[0][2]
    zCoor = resultList[0][3]
    data = resultList[0][4]
    userName = input("Type your user name")
    mpCur.execute("""UPDATE networkPlayers SET name=?, x=?, y=?, z=?, data=? WHERE username=?""", [name,xCoor,yCoor,zCoor,data,userName])
    mpDbConn.commit()
except Exception as err:
    print("something went wrong with data manipulation " + str(err))
finally:
    mpCur.close()
    spCur.close()
    mpDbConn.close()
    spDbConn.close()
