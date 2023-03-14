"""
game
"""
import my_game

antonovycha = my_game.Street("Antonovycha 61")
antonovycha.set_description("Початкова точка")

khudozhnia = my_game.Street("Khudozhnia")
khudozhnia.set_description("Спокійна тиха вуличка, з особливим калоритом")

selskykh = my_game.Street("Selskykh")
selskykh.set_description("Навесні на ній часто цвіте гарна магнолія")

zaliznyaka = my_game.Street("Zaliznyaka")
zaliznyaka.set_description("На ній розташована дитяча бібліотека, де влітку проводять майстер класи")

hipsova = my_game.Street("Hipsova")
hipsova.set_description("По особливому затишна і тиха вуличка")

konovaltsia = my_game.Street("Konovaltsia")
konovaltsia.set_description("Вуличка з старовинною архітектурою")

hordynskykh = my_game.Street("Hordynskykh")
hordynskykh.set_description("Вуличка, що веде прямо до Алтайських озер")

antonovycha.get_turn(khudozhnia, "east")
khudozhnia.get_turn(selskykh, "south")
selskykh.get_turn(zaliznyaka, "east")
zaliznyaka.get_turn(hipsova, "south")
hipsova.get_turn(konovaltsia, "east")
konovaltsia.get_turn(hordynskykh, "east")

shcherbina = my_game.Character("Щербина", "Чоловік похилого віку вчив дискретки ще самих фундаторів дискретки - Кеннет Аппеля і Вольфганг Хакена", "Якщо у вас є вибір між побаченням з дівчиною і дискретною математикою вибирайте побачення", "Колєга лєкцію вивчив?", "книга Щербини" )
khudozhnia.set_character(shcherbina)

borkivskyi = my_game.Character("Борківський(базованого)", "Вміє креативно проводити пари і дуже щедро роздає додаткові бали з ОП", "Якщо код десь падає, це не баг, а нова фіча", "Ну шо там, стендап надіюсь готовий?", "пайтон 3.11.2")
selskykh.set_character(borkivskyi)

fedynyak = my_game.Character("Фединяк", "Був колись частинкою клубу рядів Фур'є", "Всі студенти бояться цвітіння бузка, адже це означає, що сесія не за горами", "Знаєте цю формулу?", "прогулянка парком")
zaliznyaka.set_character(fedynyak)

kushnir = my_game.Character("Кушнір Морослава", "Фанатка музики", "Якщо ви купуєте сукню шоб привабити майбутнє джерело доходу, тоді це ваш актив", "Хто кращий Harry Styles чи Arctic Monkeys?", "бізнес канва")
hipsova.set_character(kushnir)

hrytsak = my_game.Character("Грицак", "Має прекрасну дружину, яка полюбляє робити продовження студентам запис лекції з виглядом на аудиторію вночі ", "Хмельницький це повне салямі. Ви ж знаєте, що таке салямі?", "Якщо будете власником готелю у Греції ви ж покличете мене на роботу у ролі садівника?", "поїздка у стародавній Єгипет")
konovaltsia.set_character(hrytsak)


book = my_game.Item("книга Щербини")
book.set_description("раритет, який за пару років коштуватиме мільйони")
khudozhnia.set_item(book)

python = my_game.Item("пайтон 3.11.2")
python.set_description("майбутнє нашого світу")
selskykh.set_item(python)

walk = my_game.Item("прогулянка парком")
walk.set_description("те, що очищує твої думки від лімітів і занурює в числові ряди")
zaliznyaka.set_item(walk)

canva = my_game.Item("бізнес канва")
canva.set_description("те, що допоможе тобі започаткувати власний бізнес і потрапити у Forbes")
hipsova.set_item(canva)

trip = my_game.Item("поїздка у стародавній Єгипет")
trip.set_description("те, що занурить тебе у стародавню атмосферу")
konovaltsia.set_item(trip)



current_street = antonovycha
backpack = []

dead = False
meet_inhabitant = 0

while dead == False:

    print("\n")
    current_street.get_details()

    if current_street.name == 'Hordynskykh':
        print('Вітаю, ти дійшов/шла до свого місця сили-Алтайських озер!')
        break

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        if not bool(meet_inhabitant):
            inhabitant.describe()
            inhabitant.description_()

    meet_inhabitant += 1

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_street = current_street.move(command)
        meet_inhabitant = 0
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.description_()
            inhabitant.base_phrase()
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Як будеш знаходити спільну мову?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.try_yourself(fight_with) <= 5:
                    # What happens if you win?
                    print("Вітаю, в тебе не талон")
                    current_street.character = None
                    if inhabitant.try_yourself(fight_with) == 5:
                        print("Вітаю, ти склав сесію")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Друже, на жаль, в тебе комісія")
                    print("Кінець укушного життя...")
                    dead = True
            else:
                print("Ти не маєш " + fight_with)
                print("На жаль, ти програв і вилетів з УКУ")
                break
        else:
            print("Ти не маєш з ким поспілкуватися")
    elif command == "take":
        if item is not None:
            print("Ти кладеш " + item.get_name() + " у свій рятівний рюкзак")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("Нема що класти до рятівного рюкзака")
    else:
        print("Не маю поняття як " + command)