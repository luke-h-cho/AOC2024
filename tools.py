def process_string_input_to_list(input: str) -> list[list[int]]:
  lines = input.strip().split("\n")
  
  num_of_columns = len(lines[0].split())

  columns = [[] for _ in range(num_of_columns)]

  for line in lines:
      values = line.split()
      for i, value in enumerate(values):
         columns[i].append(int(value))
  
  return columns
