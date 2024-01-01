# dictionary - Is a changeable, unordered collection of value:key pairs

capitals = {
    "Zimbabwe": "Harare",
    "SA": "Cape town",
    "Mozambique": "Maputo",
    "Zambia": "Lusaka"
}

#for key, value in capitals.items():
#    print(key, "->", value)

capitals.update({
    "Botswana": "Gaboroni"
})


#print(capitals.keys())
#print(capitals.values())
#print(capitals.clear())
#print(capitals.get("Zimbabwe"))
