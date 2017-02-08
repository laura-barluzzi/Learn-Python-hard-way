REGION_CAPITALS = {
    "Valle d'Aosta": "Aosta",
    "Piemonte": "Torino",
    "Liguria": "Genova",
    "Veneto": "Venezia",
    "Sardegna": "Cagliari",
    "Lombardia": "Milano",
    "Emiglia-Romagna": "Bologna",
    "Toscana": "Firenze",
    "Trentino-Alto Adige": "Trento",
    "Friuli-Venezia Giulia": "Trieste",
    "Puglia": "Bari",
    "Sicilia": "Palermo",
    "Abruzzo": "L'Aquila",
    "Marche": "Ancona",
    "Umbria": "Perugia",
    "Molise": "Campobasso",
    "Lazio": "Roma", 
    "Campania": "Napoli", 
    "Basilicata": "Potenza", 
    "Calabria": "Catanzaro"
    }
    
INHABITANTS = {
    "Milano": 1300000,
    "Venezia": 260000,
    "Belluno": 35000
    }

# ADD CITIES AND INHABITANTS

INHABITANTS["Trento"] = 110000
print "The population of Trento is %d" % (INHABITANTS["Trento"])
  
for region, capital in REGION_CAPITALS.items():
    print region, capital
    
for city, population in INHABITANTS.items():
    print "\nThe populatin of %s is: %d" % (city, population)
    
city = INHABITANTS.get("Bari", "Key not found in this library")
print city

TYPE = type(INHABITANTS["Milano"])
print "tHE DATA TYPE OF INHABITANTS IS", TYPE
