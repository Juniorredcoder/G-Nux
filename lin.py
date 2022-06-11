import os
cmd = 'clear'
os.system(cmd)
print("  ____       _   _           ")
print(" / ___|     | \ | |_   ___  __")
print("| |  _ _____|  \| | | | \ \/ /")
print("| |_| |_____| |\  | |_| |>  < ")
print(' \____|     |_| \_|\__,_/_/\_\ ')

print("                              BY G-ONE")
print("                              Version 1.01")
print("\nIf you like this follow our page :\n https://facebook.com/termux.kali4/") 
c=1
while True:
    cmd = input("\nroot@G-Nux ->")
    os.system(cmd)

c+=1
if c == 90000 :
   print('you reached limit')

