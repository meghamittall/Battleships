

data = {}
data["rows"] = 10
data["cols"] = 10
data["boardcomsize"] = 500
data["boardusersize"] = 500
data["numships"] = 5
data["cellcom"] = data["boardcom"] % (data["rows"]*data["cols"]) 
data["celluser"] = data["boarduser"] % (data["rows"]*data["cols"]) 
boardcom = emptyGrid(data["rows"],data["cols"])
boarduser = emptyGrid(data["rows"],data["cols"])
data["boarduser"] = boarduser
ship = createShip()
checkship = checkShip(boardcom,ship)
boardcom = addShips(boardcom, data["numships"])
data["boardcom"] = boardcom
return data 
data["boardcom"] = emptyGrid(data["row and col"],data["row and col"])