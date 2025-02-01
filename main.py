import datetime

def write_datetime_to_file(filename="datetime.txt"):
    """Writes the current date and time to a specified file.

    Args:
        filename: The name of the file to write to (default: datetime.txt).
    """
    try:
        now = datetime.datetime.now()  # Get current date and time
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")  # Format it
        filename = 'data/' + filename

        with open(filename, "w") as f:  # Open file in write mode ("w")
            f.write(formatted_datetime + "\n")  # Write the datetime string

        print(f"Date and time written to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # write_datetime_to_file()  # Writes to datetime.txt
    # Or specify a filename:
    write_datetime_to_file("my_log_file.txt")

