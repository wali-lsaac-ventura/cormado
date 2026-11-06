print("———cormado———")

articulos = {"pollo": 250, "agua": 25, "huevos": 10, "tomate": 15}

while True:
    
    pd = input("que tu quieres?(escribe salir o metel: )")  
    if pd == "salir":
        print("ruede mio")
        break
        
    if pd =="metel algo":
        new=input("¿que tu quieres metel?: ")
        pr=int(input("¿a cuanto lo va a poner?: "))
        articulos[new]=pr
        print(f"ya mio {new} ta listo a {pr}")
        continue
        
    if pd in articulos:
        print(f"el {pd} cuesta {articulos[pd]}")
    else:
        print("no tenemos eso mio")
        
