# Generate dict of select key:value pairs

kv_pairs = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

preferred_keys = ['a', 'c', 'e', 'g', 'i']

select_kv_pairs = dict((key, kv_pairs[key]) for key in preferred_keys if key in kv_pairs)

print(select_kv_pairs)