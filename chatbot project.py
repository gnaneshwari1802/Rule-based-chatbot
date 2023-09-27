from nltk.chat.util import Chat, reflections
# What is the full form of NLTK in chat?
# The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning functionalities.
# nltk.chat.util.Chat[source]
# Bases: object
"""
In regular expressions (regex), r"(.*)" is a pattern that matches any sequence of characters (including an empty sequence). Here's a breakdown of what each part of the pattern means:

r: This is a prefix indicating that the string should be treated as a "raw string." In Python, raw strings are often used when working with regular expressions because they prevent backslashes (\) from being treated as escape characters. This is useful because backslashes are commonly used in regex patterns, and using raw strings helps avoid conflicts.

(.*): This is the actual regex pattern. It consists of two parts enclosed in parentheses:

.: In a regex pattern, a period (.) is a metacharacter that matches any single character except for a newline character (\n). So, . matches any character.

*: The asterisk (*) is a quantifier in regex that means "zero or more occurrences of the preceding character or group." In this case, the preceding character is . (any character), so .* means "zero or more occurrences of any character."

(.*): When you enclose .* within parentheses, it forms a capturing group. This means that any sequence of characters (including an empty sequence) will be captured and can be accessed as a matched group in the regex.

Here are some examples of strings that would match the pattern r"(.*)":

An empty string: ""
A string with one character: "a"
A string with multiple characters: "hello"
A string with spaces: " " (multiple spaces)
A string with special characters: "!@#$%"
In summary, r"(.*)" is a regex pattern that can match any sequence of characters, including an empty string, and it captures the entire matched sequence as a group.





"""
# __init__(pairs, reflections={})[source]
# Initialize the chatbot. Pairs is a list of patterns and responses. Each pattern is a regular expression matching the user’s statement or question, e.g. r’I like (.*)’. For each such pattern a list of possible responses is given, e.g. [‘Why do you like %1’, ‘Did you ever dislike %1’]. Material which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to the numbered positions in the responses, e.g. %1.
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["prakash created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['our customer service will reach you']
    ],
 ]   

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)
# What are the pairs in NLTK?
# Pairs is a list of patterns and responses. Each pattern is a regular expression matching the user's statement or question, e.g. r'I like (. *)'. For each such pattern a list of possible responses is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].

chat.converse()

