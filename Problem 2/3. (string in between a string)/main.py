# Function definition for new string.
# x is a list that stores individual characters from the provided string.
# count is a variable that counts the number of characters in the provided string.
# abr is used to store the resulting 'in between string' after selecting the first, middle and last characters.
def btwn(string1, string2):
    x = []
    count = 0
    for word in range(0, len(string1)):
        count += 1
        x.append(string1[word])

    x.insert(len(string1) // 2, string2)
    abr = x
    return abr


# Main program starts here.
# word1 and word2 stores input from the user.
word1 = input("Enter the first string: ")
word2 = input("Enter the second string: ")
print("New string is :", *btwn(word1, word2), sep='')

# Sample
'''n = "Ault"
m = "Kelly"
x = []
count = 0
for word in range(0, len(n)):
    count += 1
    x.append(n[word])

x.insert(len(n)//2, m)
print(*x, sep='')'''
