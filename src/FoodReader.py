'''
Created on Nov 27, 2014

@author: James Ziemba
'''
def get_data(ratings):
    newlist = []
    # adds list of people/rest./ratings to a list
    f1 = open(ratings)
    for line in f1:
        line = line.strip()
        newlist.append(line)
    # splits items in newlist into a list of lists- even numbered indexes are people and odd numbered
    # ones are restaurant with ratings
    newer = []
    for i in newlist:
        new = i.split(',')
        newer.append(new)
    # creates dict. with people as keys and restaurants w/ ratings as values
    d = {}
    for idx in range(len(newer)):
        if len(newer[idx]) == 1:
            d[newer[idx][0]] = newer[idx+1]
    # creates new dict. with restaurants as key and values as a list of strings where string consists of
    # restaurant rater and their rating
    newd = {}
    for k,v in d.iteritems():
        for value in v:
            value = value.split(' ')
            if value[0] not in newd:
                newd[value[0]] = []
            newd[value[0]].append(k + ' '+ value[1])
            
    names = []
    restaurants = []
    #creates list of names
    for value in newd.values():
        for i in value:
            i = i.split(' ')
            if i[0] not in names:
                names.append(i[0])
    # creates list of restaurants
    for r in newd.keys():
        if r not in restaurants:
            restaurants.append(r)
    # creates list of lists in values where 0th index is name of restaurant and 1st index is its rating
    for k,v in d.iteritems():
        for i in range(len(v)):
            new = v[i].split(' ')
            v[i] = new
    # sorts names and restaurants in alphabetical order
    restaurants = sorted(restaurants)
    names = sorted(names)
    retval = {}
    #creates a place for each restaurant in values of d
    #adds rater's rating to place corresponding to restaurant if one is available
    for k,v in d.iteritems():
        retval[k] = [0 for i in range(len(restaurants))]
        for value in v:
            for r in range(len(restaurants)):
                if restaurants[r] == value[0]:
                    retval[k][r] = int(value[1])
               
    return restaurants, retval
                    
    
                
print get_data("foods.txt")              
        
    
