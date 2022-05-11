P = 23
G = 9

print('Value of P is: %d'%(P))
print('Value of G is: %d'%(G))

a = 4
print('Private key for alice is: %d'%(a))
x = int(pow(G,a,P))

b = 3
print('Private key for bob is: %d'%(b))
y = int(pow(G,b,P))

ka = int(pow(x,b,P))
kb = int(pow(y,a,P))

print('Secret key for Alice is: %d'%(ka))
print('Secret key for Bob is: %d'%(kb))