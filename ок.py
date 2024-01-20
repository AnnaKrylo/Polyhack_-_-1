import telebot
import random

bot_token = "ВАШ_ТОКЕН"
bot = telebot.TeleBot(bot_token)

parasite_dictionary = {
    "ну": ["так", "ладно", "хорошо"],
    "типо": ["примерно", "похоже]", "вроде"],
    "вроде": ["как бы", "типо", "по-видимому"],
    "как бы": ["словно", "по сути", "по-видимому"],
    "вобщем": ["в конечном счете", "в целом", "в общем-то"],
    "ваще": ["обыно", "в целом", "в общем"],
    "прикинь": ["представь себе", "вообрази", "подумай"],
    "итак": ["следовательно", "таким образом"],
    "короче": ["вкратце"],
    "вот": ["в таком контексте", "в данном случае"],
    "кстати": ["между прочим", "к слову", "кстати говоря"],
    "блин": ["безобразие", "печально", "как жаль"],
    "ешкин кот": ["безобразие", "свинство"],
    "походу": ["вероятно", "по-видимому"],
    "черт": ["досадно", "печально", "как так"],
    "то есть": ["другими словами", "в целом", "в общем"],
    "ёмаё": ["ну как так", "ничего себе"],
    "жесть": ["ничего себе", "ого"],
    "пофиг": ["все равно", "безразлично"],
    "в натуре": ["по факту", "обязательно", "конечно"],
    "ну это": ["ввиду этого", "в целом"],
    "э-э-э-э": [" "],

}


@bot.message_handler(func=lambda message: True)
def process_text(message):
    text = message.text.lower().split()

    count_parasites = 0

    for i in range(len(text)):
        word = text[i]
        if word in parasite_dictionary:
            count_parasites += 1
            synonyms = parasite_dictionary[word]

            replacement = random.choice(synonyms) if synonyms else word
            text[i] = replacement

    replaced_text = ' '.join(text)
    sentences = replaced_text.split('.')
    final_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        sentence = sentence.capitalize()
        final_sentences.append(sentence)
    final_text = '. '.join(final_sentences)
    final_text = final_text + '.'

    reply = f"Количество слов-паразитов: {count_parasites}"
    reply_2 = f"Текст после замены:\n {final_text}"
    bot.reply_to(message, reply)
    bot.reply_to(message, reply_2)


bot.polling()
