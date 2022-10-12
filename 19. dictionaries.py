
capitals = {'Sverige':'Stockholm',
            'Ryssland':'Moskva',
            'Kina':'Beijing',
            'Frankrike':'Paris'}

capitals.update({'Tyskland':'Berlin'})
capitals.update({'Sverige':'Västerås'})
capitals.pop('Kina')
capitals.clear()

#print(capitals.get['Germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals. items():
    print(key,value)