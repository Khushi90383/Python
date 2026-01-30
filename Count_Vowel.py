string="Khushi"
count=0

for char in string:
 if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        count+=1
print(f'Vowels count in string is: {count}')

string = "Khushi"
print(sum(1 for c in string.lower() if c in "aeiou"))

#How it works (quick breakdown)

#string.lower() → converts "Khushi" → "khushi"

#for c in string.lower() → iterates over each character

#if c in "aeiou" → checks if the character is a vowel

#1 for c ... → counts each vowel as 1

#sum(...) → adds all the 1s