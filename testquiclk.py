fob = open('weather.txt', 'r')
with fob as fhandle:
    
    print(fhandle.read())
    
    fhandle.close