# PZSpToMp
A simple python script that converts singleplayer player data to multiplayer player data in Project zomboid

# Requirements
Any Python version that supports sqlite3

# Explanation 
When porting a single player world to multiplayer, everything about the world file structure is the same except players.db file. Deleting the players.db file will result in a functional multiplayer world that retains all world information but not the characters. These .db or database files are SQL databases that can easily be changed. Using a visual studio code extension for SQLite we can see that “players.db” has 2 tables, localPlayers and networkPlayers. Looking into them, localPlayers is empty when the player.db file comes from a multiplayer world and networkPlayers is empty when the player.db file comes from a singleplayer world. Vise versa shows us information in the tables, screenshots below. I suspect that when a multiplayer world is being launched, the server searches for information in the networkPlayers table but doesn’t find any, thus crashes. So the solution is simple: transfer all information from localPlayers to networkPlayers. I do this by creating a new multiplayer world, grabbing the players.db file and inserting data from the singleplayer players.db file into the multiplayer one. I recognize that there could be easier ways to the solution, but I haven’t explored them yet.

# Usage
1. Navigate to the singleplayer world found under "Users\*user*\Zomboid\Saves\*difficulty*\”
2. Copy the singleplayer world into the Multiplayer folder under “Zomboid\Saves\Multiplayer”
3. Go in-game and create a server preset, making sure to include all mods that were present in the world. The name of the preset must be exactly the same as the world file name, you can change either the world name or the preset.
4. Extract the players.db file from the world and store it in the same folder as the python script.
5. Launch the game and create a character. Then exit the game.
6. Grab the newly created players.db file and drop it into the same folder as the python script. You’ll have to change one of the players.db file names.
7. Run the script and insert all of the information requested by the script. It is recommended to launch the script from the command prompt.
8. Insert the multiplayer players.db file back into the world and enjoy.

# Screenshots
Players.db table structure:
![image](https://github.com/Crayfry/PZSpToMp/assets/52294803/375bdcbd-0b3d-4a13-aa2b-9cce8002194a)

networkPlayer table from multiplayer players.db:
![image](https://github.com/Crayfry/PZSpToMp/assets/52294803/45c1c3b5-f6e1-492b-a0c6-2a58d98878d0)

localPlayer table from singleplayer players.db:
![image](https://github.com/Crayfry/PZSpToMp/assets/52294803/e77be69f-26ba-47a8-8ae0-032229e01c65)
