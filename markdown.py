# Decode Hexadecimal to Text
def hex_to_text(hex_file, output_file):
    try:
        with open(hex_file, 'r') as f:
            hex_data = f.read().replace('\n', '').replace(' ', '')
        
        # Convert hex to bytes
        binary_data = bytes.fromhex(hex_data)
        
        # Decode binary to text
        decoded_text = binary_data.decode('utf-8')  # Change 'utf-8' to appropriate encoding if needed
        
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(decoded_text)
        print(f"Decoded text saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Input hex file and output file
hex_to_text('hex_dump.txt', 'decoded_output.txt')
