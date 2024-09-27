import os
import subprocess
import sys

def install_mysql_mac(test_mode):
    print("Installing the latest version of MySQL on macOS...")
    if test_mode:
        print("Test mode: MySQL installation command will not run.")
        return
    
    try:
        subprocess.run(["brew", "install", "mysql"], check=True)
        print("MySQL installed successfully!")
    except subprocess.CalledProcessError:
        print("Error installing MySQL. Please check if Homebrew is installed and try again.")

def install_mysql_linux(test_mode):
    print("Installing the latest version of MySQL on Linux...")
    if test_mode:
        print("Test mode: MySQL installation command will not run.")
        return
    
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "mysql-server"], check=True)
        print("MySQL installed successfully!")
    except subprocess.CalledProcessError:
        print("Error installing MySQL. Please check your package manager and try again.")

def show_instructions():
    print("\nTo log in to your MySQL server, follow these steps:")
    print("1. Open your Terminal.")
    print("2. Start the MySQL service if necessary:")
    print("   - macOS: brew services start mysql")
    print("   - Linux: sudo service mysql start")
    print("3. Log in to MySQL with:")
    print("   mysql -u root -p")
    print("4. Enter your password when prompted.")
    print("   (Default configuration does not have a password, just press Enter.)")
    print("5. You can now execute SQL commands!")
    print("6. To exit, type: EXIT;")

def main():
    print("Welcome to the MySQL Installer!")
    
    # Get the operating system
    while True:
        os_type = input("Are you using macOS or Linux? (type 'mac' or 'linux'): ").strip().lower()
        
        if os_type in ['mac', 'linux']:
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please enter either 'mac' or 'linux'.")
    
    # Test mode
    while True:
        test_mode = input("Do you want to run this in test mode? (yes/no): ").strip().lower()
        
        if test_mode in ['yes', 'no']:
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
    # Convert the input to a boolean value
    test_mode = test_mode == 'yes'

    # Install based on OS type
    if os_type == 'mac':
        install_mysql_mac(test_mode)
    elif os_type == 'linux':
        install_mysql_linux(test_mode)

    # Ask user to press enter to see the MySQL login instructions
    input("\nPress Enter to see instructions on how to log in to your MySQL server...")

    # Show MySQL login instructions
    show_instructions()

    # Let the user know they can close the window when they see "[Process completed]"
    print("\nWhen you see the sentence '[Process completed]', you can close this window manually.")

if __name__ == "__main__":
    main()
