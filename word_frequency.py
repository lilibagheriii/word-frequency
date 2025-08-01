from collections import Counter

# Sample text
text = input("Enter a sentence: ")

# Remove punctuation and convert to lowercase
clean_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)

# Split into words
words = clean_text.split()

# Count word frequencies
word_counts = Counter(words)

# Print results
print("\nWord Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
