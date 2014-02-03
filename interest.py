#Rates and Calculation of Interest Models
#K(n=0) --> euros in year 0
#p --> yearly interest
#J --> yearly deposit obligation
#n --> year

import math


def recursive_model(K, p, J, n):
    acct_bal = K  #account balance

    def Kn1(K, p, J):
        return K*(1+p) + J

    for i in range(n):
        acct_bal = Kn1(acct_bal, p, J)

    return acct_bal  #balance after n years

def non_recursive_model(K, p, J, n):
    I = math.pow((1+p), n)
    return I*K +(J/p)*(I - 1) #balance after n years









