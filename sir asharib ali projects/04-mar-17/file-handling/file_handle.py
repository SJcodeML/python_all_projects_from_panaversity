# prompt: generate a comprehensive example of file handling using all the functions

# Create a file and write to it
with open('example.txt', 'w') as f:
  f.write("This is line 1.\n")
  f.write("This is line 2.\n")
  f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read the file and print its content
with open('example.txt', 'r') as f:
  content = f.read()
  print("--- Full Content ---")
  print(content)

# Read the file line by line and print each line
with open('example.txt', 'r') as f:
  print("--- Line by Line ---")
  for line in f:
    print(line, end='')

# Read a single line
with open('example.txt', 'r') as f:
  print("\n--- Readline ---")
  print(f.readline(), end='')

# Read all lines into a list
with open('example.txt', 'r') as f:
  lines = f.readlines()
  print("\n--- Readlines ---")
  for line in lines:
    print(line, end='')

# Append to the file
with open('example.txt', 'a') as f:
  f.write("This is appended line 1.\n")
  f.write("This is appended line 2.\n")

# Reading with seek and tell
with open('example.txt', 'r') as f:
  print("\n--- Seek and Tell ---")
  print("Current position:", f.tell())
  print("First line:", f.readline(), end="")
  print("Current position:", f.tell())
  f.seek(0)
  print("After seek(0):", f.tell())
  print("First line again:", f.readline(), end="")

# Demonstrating 'x' mode (exclusive creation)
try:
    with open('new_file.txt', 'x') as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")

# Copy file example
def copy_file(source, destination):
  try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
      for line in src:
        dest.write(line)
      print(f"'{source}' successfully copied to '{destination}'")
  except FileNotFoundError:
    print(f"Error: File not found '{source}'")
  except Exception as e:
    print(f"Error during copying: {e}")

copy_file("example.txt", "example_copy.txt")