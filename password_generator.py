import itertools
import string
from tqdm import tqdm  # Install with: pip install tqdm

def print_banner():
    banner = """
     ____                  ____            
    |  _ \ __ _ ___ ___   / ___| ___ _ __  
    | |_) / _` / __/ __| | |  _ / _ \ '_ \ 
    |  __/ (_| \__ \__ \ | |_| |  __/ | | |
    |_|   \__,_|___/___/  \____|\___|_| |_|
    
         Created by Technical Corp | Ethical Use Only
    """
    print(banner)

def generate_password_list():
    print_banner()
    print("### Password List Generator ###")
    print("This tool is for ethical purposes only. Use responsibly.\n")
    
    # User input
    try:
        min_length = int(input("Enter minimum password length: "))
        max_length = int(input("Enter maximum password length: "))
        if min_length > max_length:
            print("Error: Minimum length cannot be greater than maximum length.")
            return
    except ValueError:
        print("Error: Please enter valid numbers for lengths.")
        return
    
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    custom_words = input("Enter custom words (comma-separated, optional): ").split(",")
    output_file = input("Enter the output file name (e.g., passwords.txt): ").strip()

    # Build character set
    character_set = ""
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        print("Error: No character set selected. Exiting.")
        return

    # Generate passwords and write to file
    try:
        with open(output_file, "w") as file:
            print("\nGenerating passwords... This may take some time.\n")
            for length in range(min_length, max_length + 1):
                combinations = itertools.product(character_set, repeat=length)
                total_combinations = len(character_set) ** length
                for combination in tqdm(combinations, total=total_combinations, desc=f"Length {length}"):
                    file.write("".join(combination) + "\n")
            # Add custom words
            for word in custom_words:
                word = word.strip()
                if word:
                    file.write(word + "\n")
        print(f"\nPassword list successfully saved to {output_file}")
    except Exception as e:
        print(f"\nError: {e}")

# Run the tool
if __name__ == "__main__":
    generate_password_list()
