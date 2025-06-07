import streamlit as st
import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    # Define character sets
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special else ''
    
    # Combine all selected character sets
    all_chars = uppercase_chars + lowercase_chars + number_chars + special_chars
    
    if not all_chars:
        return "Error: Please select at least one character type"
    
    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_lowercase:
        password.append(random.choice(lowercase_chars))
    if use_numbers:
        password.append(random.choice(number_chars))
    if use_special:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def main():
    st.set_page_config(page_title="Password Generator", page_icon="🔑")
    
    st.title("🔑 Password Generator")
    st.write("Generate secure passwords with customizable options")
    
    # Password length
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    
    # Character type options
    col1, col2 = st.columns(2)
    with col1:
        use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
        use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
    with col2:
        use_numbers = st.checkbox("Include Numbers", value=True)
        use_special = st.checkbox("Include Special Characters", value=True)
    
    # Generate password
    if st.button("Generate Password"):
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        
        if password.startswith("Error"):
            st.error(password)
        else:
            st.success("Password Generated Successfully!")
            st.code(password, language="text")
            
            # Copy to clipboard button
            st.button("Copy to Clipboard", on_click=lambda: st.write(f"```{password}```"))
    
    # Password strength indicator
    if 'password' in locals() and not password.startswith("Error"):
        strength = 0
        if use_uppercase: strength += 1
        if use_lowercase: strength += 1
        if use_numbers: strength += 1
        if use_special: strength += 1
        if length >= 12: strength += 1
        
        st.subheader("Password Strength")
        strength_text = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
        strength_color = ["red", "orange", "yellow", "lightgreen", "green"]
        
        st.markdown(f"<p style='color:{strength_color[strength-1]}'>{strength_text[strength-1]}</p>", 
                   unsafe_allow_html=True)
    
    # Password tips
    with st.expander("Password Security Tips"):
        st.write("""
        - Use a minimum of 12 characters
        - Include a mix of uppercase and lowercase letters
        - Include numbers and special characters
        - Avoid using personal information
        - Use different passwords for different accounts
        - Consider using a password manager
        """)

if __name__ == "__main__":
    main() 