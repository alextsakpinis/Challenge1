#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:57:08 2017

@author: martin
"""
import xml.etree.ElementTree as ET
import re;

found = False;
for event, element in ET.iterparse('enwiki-20170820-pages-articles-multistream.xml'):
    
    
    for child in element:
        
        if "title" in child.tag and 'Cat' == child.text:
            for child in element.iter():
                if "text" in child.tag:
                    found = True
                    text = child.text
                    break
            if found:
                break
    if found:
        break
         
    #element.clear()
    
text = text.replace('\n', ' ').lower()

def query(queryString, text):
    queryString = queryString.replace('[', '');
    queryString = queryString.replace(']', '');
    queryString = queryString.replace(',', ' ');
    queryString = queryString.replace('"', '');

    args = queryString.split(' ')
    
    regexString = ""
    
    for i in range(0,round(len(args)/3)):
        regexString  = regexString + args[i*3] + '.{' + args[i*3+1] + ',' + args[i*3+2] + '}'

    regexString = regexString + args[-1]
    
    pattern = re.compile(regexString)
    print(pattern.findall(text))
    return
query('"cats" [0,10] "are" [0,10] "to"', text)
query('"or" [0,10] "or" [0,10] "or"', text)
query('"when" [15,25] "republic" [15,25] "along"', text)

    