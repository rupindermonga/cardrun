

def safe_float(obj):
    'safe version of float'
    try:
        retval = float(obj)
    except (ValueError, TypeError) as diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    logf = open('cardlog.txt', 'w')
    try:
        ccfile = open("carddata.txt", 'r')
    except IOError:
        logf.write('no txns this month\n')
        logf.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    logf.write('account log; \n')

    for eTxn in txns:
        result = safe_float(eTxn)
        if isinstance(result, float):
            total += result
            logf.write('data... processed\n')
        else:
            logf.write('ignored: %s' %result)
    print('$%.2f (new balance)' % total)
    logf.close()

if __name__ == '__main__':
        main()