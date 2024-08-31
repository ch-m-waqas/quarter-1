name = input("Enter your name: ")

fav_num_1 = int(input("Enter your first favorite number: "))
fav_num_2 = int(input("Enter your second favorite number: "))
fav_num_3 = int(input("Enter your third favorite number: "))
fav_num_list = [fav_num_1, fav_num_2, fav_num_3]


print(f"Hello, {name}! Let's explore your favorite numbers:")

even_odd_list = []

for num in fav_num_list:
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

for num, eo in even_odd_list:
    print(f"The number {num} is {eo}.")

squares_list = []

for num in fav_num_list:
    square = num ** 2  
    squares_list.append((num, square))

for num, square in squares_list:
    print(f"The number {num} and its square: ({num}, {square})")
sum_fav_num = fav_num_1 + fav_num_2 + fav_num_3
print(f"Amazing! The sum of your favorite numbers is: {sum_fav_num}")

is_prime = True

if num <= 1:
    is_prime = False
else:
   
    for i in range(2, int(sum_fav_num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  

if is_prime:
    print(f"Wow, {sum_fav_num} is a prime number!")
else:
    print(f"Ohh, {sum_fav_num} is not a prime number!")
