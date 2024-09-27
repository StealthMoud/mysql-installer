#!/bin/bash

echo "Welcome to the MySQL Installer (Bash Version)!"

# Check if the user wants to run in test mode
while true; do
    read -p "Do you want to run this in test mode? (yes/no): " test_mode
    test_mode=$(echo "$test_mode" | tr '[:upper:]' '[:lower:]')  # Convert to lowercase

    if [[ "$test_mode" == "yes" || "$test_mode" == "no" ]]; then
        break
    else
        echo "Invalid input. Please enter either 'yes' or 'no'."
    fi
done

# Check the operating system
while true; do
    read -p "Are you using macOS or Linux? (type 'mac' or 'linux'): " os_type
    os_type=$(echo "$os_type" | tr '[:upper:]' '[:lower:]')  # Convert to lowercase

    if [[ "$os_type" == "mac" || "$os_type" == "linux" ]]; then
        break
    else
        echo "Invalid input. Please enter either 'mac' or 'linux'."
    fi
done

# Installation based on OS
if [[ "$os_type" == "mac" ]]; then
    echo "Installing MySQL on macOS..."
    if [[ "$test_mode" == "no" ]]; then
        brew install mysql
    else
        echo "Test mode: MySQL installation command will not run."
    fi
elif [[ "$os_type" == "linux" ]]; then
    echo "Installing MySQL on Linux..."
    if [[ "$test_mode" == "no" ]]; then
        sudo apt update
        sudo apt install mysql-server
    else
        echo "Test mode: MySQL installation commands will not run."
    fi
fi

# Instructions after installation
echo -e "\nMySQL installed successfully!"

read -p "Press Enter to see instructions on how to log in to your MySQL server..."

# Instructions for logging in to MySQL
echo -e "\nTo log in to your MySQL server, follow these steps:"
echo "1. Open your Terminal."
echo "2. Start the MySQL service if necessary:"
if [[ "$os_type" == "mac" ]]; then
    echo "   - macOS: brew services start mysql"
else
    echo "   - Linux: sudo service mysql start"
fi
echo "3. Log in to MySQL with:"
echo "   mysql -u root -p"
echo "4. Enter your password when prompted."
echo "   (Default configuration does not have a password, just press Enter.)"
echo "5. You can now execute SQL commands!"
echo "6. To exit, type: EXIT;"

