# Function definition for new string.
# x is a list that stores individual characters from the provided string.
# count is a variable that counts the number of characters in the provided string.
# abr is used to store the resulting 'new string' after selecting the first, middle and last characters.
def new(string):
    x = []
    count = 0
    for phrase in range(0, len(string)):
        count += 1
        x.append(string[phrase])

    abr = x[0] + x[count // 2] + x[count - 1]
    return abr


# Main program starts here.
# Word stores input from the user.
word = input("Enter a string: ")
print("New string is :", new(word))

# Sample
'''n = "James"
x = []
count = 0
for word in range(0, len(n)):
    count += 1
    x.append(n[word])

print(x[0] + x[count//2] + x[count-1])'''
