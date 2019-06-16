import numpy as np
from scipy.optimize import minimize

def constraint2(x):
         x1=x[0];x2=x[1];x3=x[2]; x4=x[3]; x5=x[4];  x6=x[5]
         return 2.117*x1**2 + 3.546*x1*x2 + 4.512*x1*x3 + 4.694*x1*x4 + 4.154*x1*x5 \
         + 3.95*x1*x6 + 1.903*x2**2 + 3.882*x2*x3 + 4.098*x2*x4 + 3.776*x2*x5 + 3.202*x2*x6 \
         + 2.901*x3**2 + 5.574*x3*x4 + 5.402*x3*x5 + 5.522*x3*x6 + 3.935*x4**2 + 4.928*x4*x5 \
         + 4.63*x4*x6 + 2.723*x5**2 + 4.728*x5*x6 + 3.067*x6**2-2
def constraint1(x):
         return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]-1.0
def objective(x):      
         return -(12.199*x[0] + 13.171*x[1] + 13.983*x[2] + 13.735*x[3] + 13.47*x[4]+ 14.847*x[5] )
x0=[1,1,1,1,1,1]
b=(0.0,1.0)
bnds=(b,b,b,b,b,b)
con1={'type':'ineq','fun':constraint1}
con2={'type':'eq','fun':constraint2}
cons=[con1,con2]

if __name__ == '__main__':
    sol=minimize(objective,x0,method='SLSQP',\
             bounds=bnds,constraints=cons)
    print("Максимум функции доходности -%s"%str(round(sol.fun,3)))
    print("ООО TKO в Тепло   - %s, доходность- %s"%(round(sol.x[0],3),round(d[0,0]*sol.x[0],3)))
    print("ООО Термо в Тепло - %s, доходность- %s"%(round(sol.x[1],3),round(d[1,0]*sol.x[1],3)))
    print("АО МонополистТепло- %s, доходность- %s"%(round(sol.x[2],3),round(d[2,0]*sol.x[2],3)))
    print("Компания 1 - %s, доходность- %s"%(round(sol.x[3],3),round(d[3,0]*sol.x[3],3)))
    print("Компания 2 - %s, доходность- %s"%(round(sol.x[4],3),round(d[4,0]*sol.x[4],3)))
    print("Компания 4 - %s, доходность- %s"%(round(sol.x[5],3),round(d[5,0]*sol.x[5],3)))