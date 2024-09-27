# MySQL Installation Automation

This project provides an automated solution to install MySQL on both macOS and Linux systems. It guides the user through the installation process, simplifying the task by requiring only a few inputs. Users can choose between a Python script, a pre-built executable file, or a Bash script to install MySQL.

## Project Structure

- **`python-version/install_mysql.py`**: The main Python script that performs the MySQL installation. It prompts the user for the operating system and provides instructions for logging into MySQL after installation.

- **`dist/`**: Contains the executable file for users who prefer not to run the Python script manually. The executable is packaged to work independently without requiring Python or dependencies to be installed.

- **`bash-version/install_mysql.sh`**: The Bash script version of the installer. This script offers a command-line interface for installing MySQL on macOS and Linux.

## Features

- **OS Detection**: Automatically tailors the installation process based on whether you're using macOS or Linux.
  
- **MySQL Installation**: Installs the latest version of MySQL using Homebrew (for macOS) or apt (for Linux).

- **Instructions for MySQL Usage**: After installation, the program provides instructions on how to log in to your MySQL server, including:
  - Starting the MySQL service.
  - Logging in to MySQL.
  - Notes on default settings (e.g., no password required on first login).

- **Test Mode**: A test mode is available for users who want to simulate the installation process without making any actual changes to their system.

## How to Use

### 1. Using the Python Script

1. Clone the repository:
   ```bash
   git clone https://github.com/StealthMoud/mysql-installer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd mysql-installer
   ```

3. Run the Python script:
   ```bash
   python python-version/install_mysql.py
   ```

4. Follow the on-screen instructions:
   - Choose your operating system (`mac` or `linux`).
   - Opt for test mode if you don't want to actually install MySQL.
   - Follow the instructions for logging into your MySQL server after the installation.

### 2. Using the Executable File

For users who don't want to run the Python script manually, an executable version is available in the `dist/` folder. The executable can be run directly on your system without needing Python installed.

1. Go to the `dist/` folder and locate the executable file.
2. Run the executable:
   - On macOS, you might need to allow it to run from System Preferences > Security & Privacy.
   - On Linux, you might need to make it executable:
     ```bash
     chmod +x install_mysql
     ```
3. Follow the on-screen instructions for installation and MySQL login.

### 3. Using the Bash Script

For users who prefer a command-line interface, a Bash script is provided:

1. Navigate to the `bash-version/` directory:
   ```bash
   cd bash-version
   ```

2. Make the Bash script executable:
   ```bash
   chmod +x install_mysql.sh
   ```

3. Run the Bash script:
   ```bash
   ./install_mysql.sh
   ```

4. Follow the on-screen instructions for installation and MySQL login.

### 4. Logging into MySQL After Installation

After MySQL is installed, follow these steps to log in:

1. **Start the MySQL service** (if it's not already running):
   - **macOS**: 
     ```bash
     brew services start mysql
     ```
   - **Linux**: 
     ```bash
     sudo service mysql start
     ```

2. **Log in to MySQL**:
   ```bash
   mysql -u root -p
   ```
   - The default configuration does not require a password, so you can simply press `Enter` when prompted for one.

3. **Exit MySQL**:
   ```bash
   EXIT;
   ```

## Requirements

### If Using the Python Script:

- **macOS**:
  - Homebrew installed.
  
- **Linux**:
  - APT package manager (for Ubuntu/Debian-based distributions).

### If Using the Executable:

- No additional requirements. The executable is self-contained.

### If Using the Bash Script:

- The script should run on any Unix-based system (macOS or Linux) with Bash installed.

## License

This project is open-source and licensed under the MIT License.

## Contributions

Contributions to the project are welcome! Feel free to open an issue or submit a pull request to suggest improvements or report bugs.

---

Happy Installing! 🚀
