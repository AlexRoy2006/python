str_input=input("Enter a stirng:")
vowels="aeiouAEIOU"
vowel_count=0
consonants=0
for char in str_input:
    if char in vowels:
        vowel_count+=1
    else:
        consonants+=1
print(f"The number of vowels in the string {str_input} = {vowel_count}")
print(f"The number of consonants in the string {str_input} = {consonants}")