#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:09:29 2020

@author: Piyush Sambhi
 (                          (                              
 )\ )                   )   )\ )                 )    )    
(()/((  (      (     ( /(  (()/(    )    )    ( /( ( /((   
 /(_))\ )\ )  ))\ (  )\())  /(_))( /(   (     )\()))\())\  
(_))((_|()/( /((_))\((_)\  (_))  )(_))  )\  '((_)\((_)((_) 
| _ \(_))(_)|_))(((_) |(_) / __|((_)_ _((_)) | |(_) |(_|_) 
|  _/| | || | || (_-< ' \  \__ \/ _` | '  \()| '_ \ ' \| | 
|_|  |_|\_, |\_,_/__/_||_| |___/\__,_|_|_|_| |_.__/_||_|_| 
        |__/                                               

@team: R&D Team
@Contact-Details:
    Email: piyush.sambhi@denave.com
    Phone: +91-9821179339
"""


def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

