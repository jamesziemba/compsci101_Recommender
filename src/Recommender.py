'''
Created on Nov 25, 2014

@author: James Ziemba
'''
import BookReader 
blist,dbook = BookReader.get_data("books.txt", "bookratings.txt")
import FoodReader
rlist,dfood = FoodReader.get_data("foods.txt")

def averages(list, dict):
    avg = []
    for i in range(len(list)):
    #finds average of all items rated
        appval = ()
        addval = 0.0
        divval = 0.0
        for k,v in dict.iteritems():
            if v[i] != 0:
                addval += v[i]
                divval += 1
        if divval != 0.0:
            appval = (list[i],addval/divval)
            avg.append(appval)
        else:
            appval = (list[i],0)
            avg.append(appval)
    retval = []
    while len(avg) != 0:
    #sorts items in descending order according to avg. rate
        maximum = -1000
        appendval = ()
        for i in avg:
            if i[1] > maximum and i not in retval:
                maximum = i[1]
                appendval = (i[0],i[1])
        retval.append(appendval)
        avg.pop(avg.index(appendval))
    print "List of items sorted by average rating:"
    return retval
    
print averages(rlist,dfood)
    
    
def similarities(name,dict):
    base = dict[name]
    retval = []
    for k,v in dict.iteritems():
    #changes values from list of ratings to similarity score based on dot product and adds tuple
    #with name of person and sim. score to a list
        appval = ()
        if k != name:
            num = 0
            for i in range(len(v)):
                num += base[i]*v[i]
            appval = (k,num)
            retval.append(appval)
    newretval = []
    while len(retval) != 0:
    #sorts people on list by descending sim score
        max = -10000
        appendval = ()
        ix = 0
        for idx in range(len(retval)):
            if retval[idx][1] > max:
                max = retval[idx][1]
                appendval = retval[idx]
                ix = idx
        newretval.append(appendval)
        retval.pop(ix)
    print "List of people whose ratings are most similar to " + name + ":"
    return newretval


def recommended(slist,items,ratings,n):
    
    lst = slist[:n]
    #makes list of people/sim. scores 'n' items long
    namelst = []
    for i in lst:
        namelst.append(i[0])
    #makes list of names of those in lst
    for key in ratings.keys():
        if key not in namelst:
            del ratings[key]
    #deletes all keys in dict that aren't in namelst 
    d2={}
    for name in lst:
        if name[0] not in d2:
            d2[name[0]] = [name[1]]
    for name,rate in ratings.iteritems():
        for idx in range(len(rate)):
            rate[idx] = rate[idx]*d2[name][0]
    #dict where keys are people and values are their sim scores as only item in a list
    itrate = {}
    for k,v in ratings.iteritems():
        for idx in range(len(v)):
            if items[idx] not in itrate:
                itrate[items[idx]] = 0
            itrate[items[idx]] += v[idx]
    #creates dict where keys are items and values are total sim score for n most similar users
    sortlist = []
    while len(itrate) != 0:
        maximum = -100000
        delval = ''
        addval = ()
        for k,v in itrate.iteritems():
            if v > maximum:
                maximum = v
                delval = k
                addval = (k,v)
        sortlist.append(addval)
        del itrate[delval]
    #sorts books in descending order by similarity
    print "User might like these items:"
    # prints first 20 books
    return sortlist[:20]


simlist = similarities('Ben',dbook)
print simlist
print recommended(simlist,blist,dbook,20)
