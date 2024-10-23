import os


def add_language_code_to_frontmatter(folder_path, language_code):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Try reading the content of the file
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.readlines()
            except UnicodeDecodeError:
                # If UTF-8 fails, try ISO-8859-1 (or another encoding if necessary)
                with open(file_path, 'r', encoding='ISO-8859-1') as file:
                    content = file.readlines()

            # Initialize variables to track front matter
            front_matter_end = False
            new_content = []
            language_code_added = False

            # Iterate through lines to find the end of front matter
            for line in content:
                new_content.append(line)  # Add the current line
                if line.strip() == '+++':
                    if not front_matter_end:
                        front_matter_end = True  # Mark that we are now in the content
                    else:
                        if not language_code_added:
                            new_content.insert(-2,
                                               f'languageCode = "{language_code}"\n')  # Add language code before the last +++
                            language_code_added = True  # Mark that we added the language code

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_content)


# Specify the folder path and the language code
folder_path = 'Posts_en'  # Replace with your folder path
language_code = 'en'

# Call the function
add_language_code_to_frontmatter(folder_path, language_code)