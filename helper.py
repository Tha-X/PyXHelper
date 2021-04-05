def my_print(string, num_chars):
  num_lines = int(len(string)/num_chars)
  for i in range(num_lines):
    print(string[(i * num_chars):((i+1) * num_chars)])
  print(string[(num_lines * num_chars):])