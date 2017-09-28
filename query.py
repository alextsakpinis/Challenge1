import re
"""
query : the asked query function. Takes the asked string as parameter (see statement)
"""

def query(queryString, text):
    print(text)
    #Get the proper arguments in the string
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
    
    pattern = re.compile(regexString)
    pattern.findall(text)
    return