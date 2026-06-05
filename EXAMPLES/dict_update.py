spam = {
    'a': 10,
    'b': 20,
    'c': 30,
}

ham = {
    'c': 100, # will overwrite existing value
    'd': 200,
    'e': 300,
}

eggs = {
    'e': 1000,
    'f': 2000,
    'g': 3000,
}
# new way as of v3.9
spam |= ham  # overwrite existing values; add new values
print(f"{spam = }")

# previous way (still works)
spam.update(eggs)
print(f"{spam = }")
