# ---------------------------------Normal-----------------------------
# numbers = []
# for i in range(5):
#     numbers.append(i)
# print(numbers)


# ------------------------List comprehension---------------------
"""squares"""
# squares = [x * x for x in range(1, 11)]
# print(squares)

"""Even"""
# evens = [x for x in range(1, 21) if x % 2 == 0]
# print(evens)

"""Length of each word"""
# words = ["python", "java", "c"]
# lengths = [len(w) for w in words]
# print(lengths)


# ----------------------Set Comprehension------------------------
# nums = [1, 2, 2, 3, 4, 4]
# unique = {x for x in nums}
# print(unique)

# -------------------------Dictionary Comprehension----------------------------
# ===========normal=================
# d = {}
# for i in range(3):
#     d[i] = i*i
# print(d)

# =================Dictionary comprehension:==================
"""Number -> Square"""
# squares = {x: x*x for x in range(1, 6)}
# print(squares)

"""Word -> Length"""
# words = ["cat", "tiger", "lion"]
# lengths = {w: len(w) for w in words}
# print(lengths)


# ==================Nested Comprehension=======================
# matrix = [[1, 2], [3, 4], [5, 6]]
# flat = [n for row in matrix for n in row]
# print(flat)
