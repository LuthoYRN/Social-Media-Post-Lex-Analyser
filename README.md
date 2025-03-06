# Social Media Post Lexical Analyser

This program performs lexical analysis on files containing messages or posts, similar to those found in instant messaging or social media applications. It identifies words, numbers, whitespace, punctuation, hashtags, name references, and illegal characters.

How to Run?

- Clone the repository:
 ```sh
   git clone https://github.com/LuthoYRN/social-media-post-lex-analyser.git
   ```
- Navigate to the directory containing lex_msg.py:
 ```sh
   cd "social-media-post-lex-analyser"
   ```

- Run the lexical analyser with a .msg file as input:
 ```sh
   python3 lex_msg.py <filename>.msg
   ```

Expected Output

- It saves the tokens to a .tkn file with the same name as the input.
