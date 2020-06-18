#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:10:33 2020

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


def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
