# Coding:
# if the word contains atleast 3 characters, 
# remove the first letter and append it at the end now append three random characters at the starting and the end 
# else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, 
# reverse it else: remove 3 random characters from start and end. 
# Now remove the last letter and append it to the beginning

import random
import string

st = input("Enter the message: ")
words = st.split(" ")
coding = input("Do you want to code or decode? (1-code/0-decode): ")
coding = True if coding == '1' else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if (len(word) >=3):
            r1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("ENCODED: ", " ".join(nwords))

else:
    nwords = []
    for word in words:
        if (len(word) >=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("DECODED: ", " ".join(nwords))
