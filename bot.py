from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla|hola)',['hey there','hi there','haayyy']],
    ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?','Tokyo, Japan'],
    ['(.*) created you ?',['Fi@m@n the best did using NLTK']],
    ['how is the weather in (.*)',['the weather in %1 is amazing like always']],
    ['(.*)help(.*)',['can I help you?']],
    ['(.*) your name ?',['my name is T.R.A.I.L__FIRST FIRA']]
    #['(.*) what can you do?',['I am now limited with some and specicfic abilities to know my name and greeting and some other extra stuffs so enkulal kes be kes beigiru yihedal']]




]

my_dummy_reflections ={
    'go':'gone',
    'hello':'hey there'
    }

print('I am a chat bot of sinqe bank')
chat = Chat(pairs,my_dummy_reflections)
chat.converse()