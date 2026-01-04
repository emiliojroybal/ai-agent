import functions.get_file_content

print(functions.get_file_content.get_file_content("calculator", "lorem.txt"))
print(functions.get_file_content.get_file_content("calculator", "main.py"))
print(functions.get_file_content.get_file_content("calculator", "pkg/calculator.py"))
print(functions.get_file_content.get_file_content("calculator", "/bin/cat"))
print(functions.get_file_content.get_file_content("calculator", "pkg/does_not_exist.py"))