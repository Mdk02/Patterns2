import pandas as pd
import pickle

import preprocessing as preprocessing

df = pd.read_csv('res.csv')
df2 = pd.read_csv('df.csv')
model = pickle.load(open('model.sav', 'rb'))

"""
df2['properties.severity'] = df2['properties.severity'].map({'Легкий' : 1, 'Тяжёлый' : 2, 'С погибшими' : 3})

le1 = preprocessing.LabelEncoder()
df2['properties.light'] = le1.fit_transform(df2['properties.light'])

le2 = preprocessing.LabelEncoder()
df2['properties.nearby'] = le2.fit_transform(df2['properties.nearby'])

le3 = preprocessing.LabelEncoder()
df2['properties.weather'] = le3.fit_transform(df2['properties.weather'])

le4 = preprocessing.LabelEncoder()
df2['properties.category'] = le4.fit_transform(df2['properties.category'])

le6 = preprocessing.LabelEncoder()
df2['properties.road_conditions'] = le6.fit_transform(df2['properties.road_conditions'])

le7 = preprocessing.LabelEncoder()
df2['properties.participant_categories'] = le7.fit_transform(df2['properties.participant_categories'])
"""


def bot_say(mes):
    print(f"bot: {mes}")


def commands():
    print("bot: Я умею: ")
    print("1)'Определить' - по введеному городу и уровню опасности вывести все адреса, подходящие под условия")
    print("2)'Справка' - вывести список команд")
    print("3)'Уровень' - показать уровни опасности")
    print("4)'Возле' - показать, какие объекты могли быть рядом")


def get_levels():
    return "1 - относительно безопасно,\n2 - средняя опасность,\n3 - довольно опасно"


def commands_for_tk():
    return "bot: Я умею: \n1)'Определить' - по введеному городу и уровню опасности вывести все адреса, \nподходящие под условия\n2)'Справка' - вывести список команд\n3)'Уровень' - показать уровни опасности"


def get_data(city, lvl):
    indexes = df[df['properties.region'] == city].index.tolist()
    if len(indexes) == 0:
        return "такого города нет"
    if lvl != '1' and lvl != "2" and lvl != '3':
        return "такого уровня нет"
    if lvl == "1":
        lvl = "относительно безопасно"
    elif lvl == "2":
        lvl = "средняя опасность"
    elif lvl == "3":
        lvl = "довольно опасно"
    return df[(df['properties.region'] == city) & (df['level'] == lvl)]['properties.address']


#для консоли
if __name__ == '__main__':
    commands()
    while True:
        bot_say('Введите команду')
        com = input('user: ')
        if com == "Справка":
            commands()
        elif com == 'Уровень':
            bot_say(get_levels())
        elif com == 'Определить':
            city = input('user: Город - ')
            indexes = df[df['properties.region'] == city].index.tolist()
            if len(indexes) == 0:
                bot_say('Такого города нет')
                continue
            lvl = input('user: Уровень опасности - ')
            if lvl != '1' and lvl != "2" and lvl != '3':
                bot_say("такого уровня опасности нет")
                continue
            if lvl == "1":
                lvl = "относительно безопасно"
            elif lvl == "2":
                lvl = "средняя опасность"
            elif lvl == "3":
                lvl = "довольно опасно"

            bot_say(df[(df['properties.region'] == city) & (df['level'] == lvl)]['properties.address'])
        elif com == 'Пред':
            print('Все поля свыше')
            pred = model.predict("все что было получено")
            if pred == 1:
                print()
            elif pred == 0:
                print()
            elif pred == 2:
                print()
