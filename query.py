import re
"""
createRegex : create a regex from a query string (as specified in the statement)
                 Takes the asked string as parameter (see statement)
"""

def createRegex(queryString):
    #Get the proper arguments in the string
    #Remove useless characters
    queryString = queryString.replace('[', '')
    queryString = queryString.replace(']', '')
    queryString = queryString.replace(',', ' ')
    queryString = queryString.replace('"', '')

    args = queryString.split(' ')
    
    #Create the regex acoording to the query string
    regexString = ""
    
    for i in range(0,round(len(args)/3)):
        regexString  = regexString + args[i*3] + '.{' + args[i*3+1] + ',' + args[i*3+2] + '}'

    regexString = regexString + args[-1]
    
    #create the pattern matcher
    pattern = re.compile(regexString)
    return pattern