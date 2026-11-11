name=input("Enter the name:")
city=input("Enter city name:")
print("Hello", name, "!welcome to", city)
# f fomated
print(f"Hello {name}! Welcom to, {city}")


#Define Message Templates


from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

simple_prompt = "THE {subject} is strong in this one."
human_prompt = "Summarize our conversation so far in {word_count} words."

simple_message_template = HumanMessagePromptTemplate.from_template(simple_prompt)
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name='conversation'),
    simple_message_template,
    human_message_template,
])

conversation = [
    HumanMessage(content="What's the best way to learn a new language?"),
    AIMessage(content="1. Immerse yourself in the language: Try to use the language in your daily life as much as possible.\n\n2. Practice regularly: Consistency is key when learning a new language.\n\n3. Use language learning apps: There are many apps that can help you learn a new language in a fun and engaging way.")
]

result = chat_prompt.invoke({
    'conversation': conversation,
    'subject': 'Force',
    'word_count': '10',
})
print(type(result))
print(result)
print(result.to_messages())

for message in conversation:
    print(message.type, message.content)