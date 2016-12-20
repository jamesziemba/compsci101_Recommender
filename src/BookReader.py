'''
Created on Nov 25, 2014

@author: James Ziemba
'''
def get_data(books,ratings):
        booklist = []
        newlist = []
        rdict = {}
        #adds data from books file to a list
        f = open(books)
        for line in f:
            name = line
            name = name.strip()  
            booklist.append(name)
        f.close()
        # adds data from ratings file to a list
        f1 = open(ratings)
        for line in f1:
            line = line.strip()
            newlist.append(line)
        f1.close()
        # splits newlist of people & ratings into a dict- people are keys and ratings are values
        for i in range(len(newlist)):
            if i % 2 != 0:
                k = newlist[i].split(' ')
                newlist[i] = k
        for i in range(len(newlist)):
            if i % 2 == 0:
                rdict[newlist[i]] = []
            else:
                for j in newlist[i]:
                    rdict[newlist[i-1]].append(int(j))
        return booklist, rdict
    
        

