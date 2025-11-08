# num_10 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# for n in num_10:
#     print(n)

# total = 0
# for n in num_10:
#     total += n
# print("Сумма всех", total)

# min_num_10 = num_10[0]
# max_num_10 = num_10[0]

# for n in num_10:
#     if n < min_num_10:
#         min_num_10 = n
#     if  n > max_num_10:
#         max_num_10 =n
# print(min_num_10, max_num_10)

# names = ["Алина", "Бек", "Саша", "Женя", "Тима", "Айза"]

# user_names = []

# for name in names:
#     if len(name) > 4:
#         user_names.append(name)
# print(user_names)


# numbers = [3, 7, 2, 9, 5]

# max_num = numbers[0]
# max_index = 0

# for i in range(len(numbers)):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#         max_index = i

# print(max_index)


#7  def get_index(lst, value):
#     for i in range(len(lst)):
#         if lst[i] == value:
#             return i
#     return -1

# numbers = [11, 12, 21, 23, 24, 25]
# print(get_index(numbers, 4))
# print(get_index(numbers, 24))

# word = ["кошка", "собака", "кролик", "черепаха"]

# word_lengt = {}

# for word in word:
#     word_lengt[word] = len(word)

# print(word_lengt)


nums = [3, 8, -2, 5, 10, -7]

# positive_nums = list(filter(lambda x: x > 0, nums))
# print(positive_nums)

# result_nums = list(map(lambda x: abs(x) * 2, nums))
# print(result_nums)

# students = [{"name": "Алина", "grade": 120},
#             {"name": "саша", "grade": 70},
#             {"name": "Аня", "grade": 80},
#             {"name": "Женя", "grade": 40}
# ]

# sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
# for student in sorted_students:
#     if student["grade"] < 70:
#         print(student["name"], student["grade"], "стрем")
#     else:
#         print(student["name"], student["grade"])

# from datetime import datetime

# user_input = input("Введите сообщение: ")
# current_time = datetime.now().strftime("%y-%m-%d  %H:%M:%S")

# log_entry = f"[{current_time}] {user_input}\n"

# with open("log.txt", "a", encoding="utf-8") as file:
#     file.write(log_entry)
# print("сообщение записано :)")


#частата слов

