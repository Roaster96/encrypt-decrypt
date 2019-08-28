x= "Project on encryption and decryption by Sarthak"
y= x.center(150)
print()
print(y)
for q in range(0,2):
    print()
alpha = "abcdefghijklmnopqrstuvwxyz"
key = 9
newmsg = ''
message=input("Enter your message to encrypt : ")


for i in message:

    pos = alpha.find(i)
    newposition=(pos+key)%26
    newchar=alpha[newposition]
    newmsg+=newchar

print("The encrypted message is : ",newmsg)

print()
print()
message=input("Enter your message to Decrypt : ")

dmsg=''
for i in message:

    pos = alpha.find(i)
    newposition=(pos-key)%26
    newchar=alpha[newposition]
    dmsg+=newchar

print("The decrypted message is : ",dmsg)

