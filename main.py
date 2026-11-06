from pyscript import document,display

# all non-metal elements
element = {"Hydrogen" : ("H", 1, 1.0079), "Helium" : ("He", 2, 4.0026), "Carbon" : ("C", 6, 12.0107), "Nitrogen" : ("N", 7, 14.0067), "Oxygen" : ("O", 8, 15.9994), "Fluorine" : ("F", 9, 18.9984), "Neon" : ("Ne", 10, 30.1797), "Phosporus" : ("P", 15, 30.9738), "Sulfur" : ("S", 16, 32.065), "Chlorine" : ("Cl", 17, 35.453), "Argon" : ("Ar", 18, 39.948), "Selenium" : ("Se", 34, 78.96), "Bromine" : ("Br", 35, 79.904), "Krypton" : ("Kr", 36, 83.798), "Iodine" : ("I", 53, 126.9045), "Xenon" : ("Xe", 54, 131.293), "Radon" : ("Rn", 86, 222.0)}

# function to search your element
def search_element(e):
    # get input from HTML
    element_1 = document.getElementById("element1").value.title()
    # retrieve information
    results = element.get(element_1, ('Element not found', '-', '-'))
    # display the result in HTML
    document.getElementById('code').innerText = element_1
    document.getElementById('symbol').innerText = results[0]
    document.getElementById('order').innerText = results[1]
    document.getElementById('mass').innerText = results[2]
