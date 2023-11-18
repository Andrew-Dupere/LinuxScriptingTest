



# Function to replace a specific line in an HTML file
from datetime import datetime


html_file_path = r"/var/www/html/index2.html"
line_number = 19
new_content = 'last update' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


def replace_line_in_html(html_file_path, line_number, new_content):
    with open(html_file_path, 'r') as file:
        lines = file.readlines()

    if 0 < line_number <= len(lines):
        lines[line_number - 1] = new_content

        with open(html_file_path, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number} replaced successfully.")
    else:
        print(f"Invalid line number: {line_number}")


replace_line_in_html(html_file_path, line_number, new_content)

