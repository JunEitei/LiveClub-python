from fontTools.ttLib import TTFont


def convert_ttf_to_woff2(input_file, output_file):
    # Load the TTF font
    font = TTFont(input_file)

    # Set flavor to woff2
    font.flavor = 'woff2'
    font.save(output_file)


# Example usage
convert_ttf_to_woff2('Hina-Mincho-Regular.ttf', 'Hina-Mincho-Regular.woff2')