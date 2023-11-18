



# Function to replace a specific line in an HTML file
def replace_line_in_html(html_file_path, line_number, new_content):
    with open(html_file_path, 'r') as file:
        lines = file.readlines()

    if 0 < line_number <= len(lines):
        lines[line_number - 1] = new_content + '\n'

        with open(html_file_path, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number} replaced successfully.")
    else:
        print(f"Invalid line number: {line_number}")

# Specify the path to your HTML file
html_file_path = 'path/to/your/file.html'

# Specify the line number you want to replace
line_number_to_replace = 5

# Specify the new content to replace the line
new_content = '<p>New content for the line</p>'

# Replace the specified line in the HTML file
replace_line_in_html(html_file_path, line_number_to_replace, new_content)
