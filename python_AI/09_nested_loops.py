colors = ['red', 'green', 'blue']
items = ['book', 'pen', 'copy']

# for color in colors:
#     for item in items:
#         print(color, item)

# # nested while loop
# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i,j)
#         j+=1
#     i += 1


# how to stop infinite loop ctrl + c in terminal

i = 1 
while i < 4:
    for j in range(3):
        print(i,j)
    i+=1