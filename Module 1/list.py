
# metingen_science_park = [12.7, 18.8, 24.9, 14.5, 19.0]
# metingen_science_park.append(20.5)
# for meting in metingen_science_park:
metingen_science_park = [12.7, 18.8, 24.9, 14.5, 19.0]
metingen_science_park.append(20.5)
for positie in range(0, len(metingen_science_park)):
    print positie+1,
    print " de meting was", metingen_science_park[positie], "graden"
print len(metingen_science_park)