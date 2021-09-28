cell = data["cell"]
    for i in range(data["row and col"]):
        for j in range(data["row and col"]):
            if grid[i][j] == SHIP_UNCLICKED:
            
                color = "blue"
            x1 = 50*j
            y1 = 50*i
            x2 = x1 + 50
            y2 = y2 + 50
         canvas.create_rectangle(x1, y1, x2, y2, outline='black')
        

        
