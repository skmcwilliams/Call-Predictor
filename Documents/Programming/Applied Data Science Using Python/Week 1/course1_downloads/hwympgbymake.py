import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))


vehiclemake = set(d['manufacturer'] for d in mpg) # what are the makes
#vehiclemanufacturer 
HwyMpgByMake = []

for t in vehiclemake: # iterate over all the vehicle makes
    summpg = 0
    vmakecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['manufacturer'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vmakecount += 1 # increment the count
    HwyMpgByMake.append((t, summpg / vmakecount)) # append the tuple ('make', 'avg mpg')

HwyMpgByMake.sort(key=lambda x: x[1]) #sort lowest mpg to highest
HwyMpgByMake
print(HwyMpgByMake)