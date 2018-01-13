# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:26:34 2018

@author: actionfocus
"""
def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    else:
        print 'no Value or Type Error.\n'
    finally:
        print obj+', this line is processed.\n'
    return retval

def main():
    'handles all the data processing'
    log = open('c:/laptop/00Python/testdata/cardlog.txt','w')
    try:
        ccfile = open('c:/laptop/00Python/testdata/carddata.txt','r')
    except IOError, e:
        log.write('no txns this month.\n')
        log.close()
        return
    
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')
    
    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data ... processed.\n')
        else:
            log.write('ignored: %s' % result)
    print '$%.2f (new balance)' % (total)
    log.close()
    
if __name__ == '__main__':
    main()
