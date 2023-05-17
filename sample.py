from langdetect import detect

text = "bonjour tout le monde"

# Detect the language of the text
language = detect(text)

# Print the detected language
print("Detected language:", language)
