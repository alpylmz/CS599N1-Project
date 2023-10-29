for i in range(100):
    local_filename=f"{i}/kernprof_output.txt"
    str_name="*** PROFILING RESULTS [ms]"
    file = open(local_filename, "r")
    lines = file.readlines()
    for line in lines:
        if str_name in line:
            print("Find")
            start = lines.index(line)
            # lines = lines[start::1]
            lines = lines[start:-3:1]
            break
    file.close()
    file = open(local_filename, "wt")
    for line in lines:
        file.write(f"{line}")
    file.close()


# import os

# # Specify the root directory where you want to start the search
# root_directory = './data'

# # Define a function to update the content of "a.txt" in a specific folder
# def update_a_txt_in_folder(folder_path):
#     a_txt_path = os.path.join(folder_path, "kernprof_output.txt")
#     if os.path.exists(a_txt_path):
#         file = open("kernprof_output.txt", "r")
#         lines = file.readlines()
#         for line in lines:
#             if "*** PROFILING RESULTS [ms]" in line:
#                 print("Find")
#                 start = lines.index(line)
#                 # lines = lines[start::1]
#                 lines = lines[start:-3:1]
#                 break
#         file.close()
#         file = open("kernprof_output.txt", "wt")
#         for line in lines:
#             file.write(f"{line}")
#         file.close()

# # Recursively traverse subfolders and update "a.txt" in each folder
# for folder_name, subfolders, files in os.walk(root_directory):
#     if "kernprof_output.txt" in files:
#         update_a_txt_in_folder(folder_name)

# print("Text file 'a.txt' updated in all relevant folders.")
