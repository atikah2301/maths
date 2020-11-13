#Super Anagram Checker#

#A super anagram of a string has the same first and last character as the string
#and contains exactly all the same interior characters, although the order may vary
#needs to be updated to only count distinct instances of a letter
#otherwise an example such as "upper uprer" is considered a super anagram

x = str(input("Enter a pair of words: "))
x = list(x.split())

while len(x) != 2:   #input should only be exactly two words
   x = str(input("Pairs only. Try again: "))
   x = list(x.split(" "))
   if len(x) == 2:
      break

if len(x[0]) == len(x[-1]): #if the two words are the same length
   i = 0
   checks = []
   if x[0][0] == x[-1][0] and x[0][-1] == x[-1][-1]: #and if the first letters and last letters are the same
         for i in range(0,len(x[0])):  #checking each letter of the word
            if x[0][i] in x[-1] and x[-1][i] in x[0]:  #if an instance of letters in one word exist in the other
               checks.append(True)   #create a list of true false values corresponding to each letter
            else:
               checks.append(False)
         
         if all(checks):   #only if "checks" consists exclusively of true values
            print("Super Anagram!")
         else:
            print("Not a super anagram")

   else:
      print("Not a super anagram")

else:
   print("Not a super anagram")
