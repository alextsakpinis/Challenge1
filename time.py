#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:57:08 2017

@author: martin
"""
from query import query
from lxml import etree

found = False;

#precompiled xpath queries
title = etree.XPath('x:title', namespaces = {'x' : 'http://www.mediawiki.org/xml/export-0.10/'})
textTag = etree.XPath('x:revision/x:text', namespaces = {'x' : 'http://www.mediawiki.org/xml/export-0.10/'})

#Run trough the whole Wikipeadia file and look at every page tag
for event, element in etree.iterparse('enwiki-20170820-pages-articles-multistream.xml', events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page'):
    
    #Takes the text section of every page tag and saves it in a variable
    text = textTag(element)[0].text            
    
    #Run the queries on the previous saved text
    query('"cats" [0,10] "are" [0,10] "to"', text)
    query('"or" [0,10] "or" [0,10] "or"', text)
    query('"when" [15,25] "republic" [15,25] "along"', text) 
    
    #Clear the element from the memory in order to be able to go through the whole Wikipedia file
    element.clear()
    while element.getprevious() is not None:
        del element.getparent()[0]
    
