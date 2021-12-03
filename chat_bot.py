#Description: This is a chat bot program 

from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)',['hi %1']],
    ['(hi|hello|hey|holla|hola',['hey there','hi there','haayyyy']],
    ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],
    ['(.*)(location|city)?',['Tokyo,Japan']],
    ['how is the weather in (.*)',['the weather in %1 is good']]

    
]

chat = Chat(pairs,reflections)
chat._substitute('you are amazing')
#chat.converse()

print(reflections)