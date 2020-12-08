import sys
from os import path, getcwd
from time import perf_counter

def read_file(filename):
  try:
    # with open(filename) as f:
    #     content = f.readlines()

    # content = [info.strip() for info in content]

    content = open(filename).read().split('\n\n')

  except:
    print('Error to read file')
    sys.exit()

  return content

def count_yes(data):
  return sum(
    [
      len(set(item.replace('\n', ''))) 
      for item in data
    ]
  )
if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    result = count_yes(data=input_data)

    print(f'Result: {result}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)