# Password Generator

A secure password generator built with Streamlit that helps you create strong, customizable passwords.

## Features

- Customizable password length (8-32 characters)
- Multiple character type options:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Password strength indicator
- Copy to clipboard functionality
- Password security tips
- Clean and intuitive user interface

## Setup

1. Make sure you have Python installed on your system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Password Generator, navigate to the project directory and run:
```bash
streamlit run src/app.py
```

## Usage

1. Adjust the password length using the slider
2. Select the character types you want to include
3. Click "Generate Password" to create a new password
4. Use the "Copy to Clipboard" button to copy the password
5. Check the password strength indicator
6. View password security tips in the expandable section

## Security Features

- Ensures at least one character from each selected type
- Randomly shuffles the password
- Provides password strength feedback
- Includes security best practices

## PowerPoint Presentation Prompts

1. Introduction to Password Generator
   - Title: "Building a Secure Password Generator"
   - Key points: Project overview, features, security importance

2. User Interface Design
   - Title: "User Interface and Experience"
   - Key points: Layout, customization options, feedback system

3. Technical Implementation
   - Title: "Technical Architecture and Implementation"
   - Key points: Password generation algorithm, security measures

4. Features and Functionality
   - Title: "Generator Features and Security"
   - Key points: Customization options, strength indicators, security tips

5. Future Enhancements
   - Title: "Future Improvements and Extensions"
   - Key points: Additional security features, password management, user preferences 