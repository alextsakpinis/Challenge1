#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:57:08 2017

@author: martin
"""
from query import query
from lxml import etree
import re

found = False;

#precompiled xpath queries
title = etree.XPath('x:title', namespaces = {'x' : 'http://www.mediawiki.org/xml/export-0.10/'})
textTag = etree.XPath('x:revision/x:text', namespaces = {'x' : 'http://www.mediawiki.org/xml/export-0.10/'})

for event, element in etree.iterparse('enwiki-20170820-pages-articles-multistream.xml', events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page'):
    
    if re.match('[Aa]',title(element)[0].text):
        text = textTag(element)[0].text            
        
        if text != None:
    
            query('"cats" [0,10] "are" [0,10] "to"', text)
            query('"or" [0,10] "or" [0,10] "or"', text)
            query('"when" [15,25] "republic" [15,25] "along"', text)          
         
    element.clear()
    while element.getprevious() is not None:
        del element.getparent()[0]
    

