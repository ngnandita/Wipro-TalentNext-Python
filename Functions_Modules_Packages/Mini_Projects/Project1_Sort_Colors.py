"""
Project Name : Sort Colors
Module       : Functions/Modules/Packages
"""

def sort_colors(colors):
    color_list = colors.split('-')
    color_list.sort()
    return '-'.join(color_list)

colors = input("Enter colors separated by hyphen: ")

print("Sorted colors:")
print(sort_colors(colors))