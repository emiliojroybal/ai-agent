import functions.get_files_info

print(functions.get_files_info.get_files_info("calculator", "."))
print(functions.get_files_info.get_files_info("calculator", "pkg"))
print(functions.get_files_info.get_files_info("calculator", "/bin"))
print(functions.get_files_info.get_files_info("calculator", "../"))