
* add docstrings to all the functions
* formato estandard del output
* preguntas especificas
* make boleeeans about lkike what the user wants to run and then run it
* sort date exmaple
* maybe we can ask the model to follow a series ot solve the queri
* make step by step instructions and function
*  next steps audio would be cool follow up queries set up default locatio + user? 
* (depends one how we want to do it)

* before enetreing teh call put a message that sais smt like: "Searching for news related to ___"


* scraping for follow up quetsions only (tell the user that you can explain further any article)


Escenario ideal:

User: "tell me about news yesterday on sports"

Backend -> 10 article titles and tell it to summarize into one short sentence. Follow up if he wants the user to go into a specific article of the

System:
* I found several news that talk about
- Football
- Hockey

User:
* Tell me about football

System:
* I found several news that talk about football
* Mention Titles (2-5 words)  summarized
* Which one would you like me to tell you about?

User: Tell me about the world cup article

Backend -> Select one of the articles, scrap it and tell it to the user in a short setence with bullet points.

System:
Great! The article says:
- Messi scored a goal
- Ronaldo scored a goal
- Brazil won the world cup
- Argentina lost the world cup


* Keyword vs category
* sport vs smt super speicfi like gaza


* make the focus a conversation style