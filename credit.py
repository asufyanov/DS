def getMonthPayment(sum, proc, n):

    coff = (proc*(pow(1+proc, n)))/(pow(1+proc, n)-1)
    return coff * sum

sum = float(input())
proc = float(input())/12/100
n = float(input())

print(getMonthPayment(sum, proc, n))
