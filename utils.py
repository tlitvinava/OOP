def convert_color_to_ansi(color_name):
    color_map = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "black": "\033[30m",
    }
    reset_code = "\033[0m"
    return color_map.get(color_name.lower(), reset_code)
