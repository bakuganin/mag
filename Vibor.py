import random
life = 1
day = 1
year = random.randint(0,400)
print("Привет! Выбери за кого будешь играть:")
print("Выбери цифру [1] - маг стихийный [2] - маг темный [3] - маг светлый")
mag = int(input())
if mag == 1:
   print("Теперь ты - стихийный",)
elif mag == 2:
    print("Теперь ты - тёмный")
else:
    print("Теперь ты - светлый",)

print()
print("Пошли вы в путь за познанием смысла жизни, свою силу и найти своего наставника, какторый наставит его на пусть праведный.")
print()
print("Год - ", year,"День - ",day)
way = int(input("Да, начнется ваш путь - Шёл он, шёл, пришёл набрёл на дорогу [Выбор] ((1)лес или (2)деревня)"))
if way == 1 or 2:
    print("Да наткнулся он дикого вепря, думает...")
    way = int(input("[Выбор] - ((1)сбежать или (2)остаться)"))
    if way == 2:
        print("Вы умерли.")
        exit
    else:
        print("Выбор стал верным, решил маг сбежать, т.к понимал, что у него нет столько сил, дабы победить даже обычного зайца, поэтому ему приходится бежать, или смерть")
        print()
        print("И вот, сбежал он дальше, по пути наткнувшись на реку. Решил, он умыться в этой реке, да вот снова неожиданный поворот его настал, вылезла перед ним(Тварь заморзкая или русалка)")
        print("Встал перед ним снова [ВЫБОР] ((договориться) - если русалка, (прикончтиться) если тварь")
        print()
        monster = random.randint(1,2)
        if monster == 2:
            print("Ты сдох.")
            exit
        else:
            print("Вот он снова избавился от своей проблемы, договорившись с русалкой, да пошел он дальше, дабы с пути не сбиться.")
            print("Спустя сутки...")
            print()
            print("Шел маг целые сутки, предстал перед ним выход в страаашное подземелье.")
            print("И настал выбор.")
            print("[ВЫБОР] - ((1)войти или (2)обойти)")
            way = int(input())
            if way == 2:
                print("Набрёл на огромную шайку бандитов, который обокрали его, избили да прикончили его. Вот и все конец его путешествия!")
                print("Ты проиграл!")
                exit
            else:
                print("Бродил он себе по пещере этой злостной, да набрел он на сундук, да вот он заперт. Придется ему искать ключ от него.")
                monster = random.randint(1,2)
                if monster == 1:
                    print("Начал искать он ключ от сундука, пока искал он ключ этот, набрёл он на говорящую жабу, у которой был электро-посох")
                    way = int(input("[ВЫБОР] - ((1)сбежать или (2)сразиться)"))
                    if way == 1:
                        print("Вы умерли от электро-снаряда жабы.")
                        print("Вы проиграли!")
                        exit
                elif monster == 2:
                    print("Начал искать он ключ от сундука, пока искал он ключ этот, набрёл он на амфибию")
                    way= int(input("[ВЫБОР] - ((1)свалить или (2)переговорить(о его государстве))"))
                    if way == 2:
                        print("Маг высказался о нём, его народе, власти достаточно плохо.")
                        print("Амфибия убила вас! GAME OVER))")
                        exit
                    else:
                        print("Маг сбежал. И вот, шёл он дальеше, наткнулся на сидящего на камне старика  с деревянным посохом(в общем тоже маг)")
                        print("и, кажется, ключ у этого мага. Ключ нужен нашему магу, поэтому он подошёл к старику, да стал просить его.")
                        print("А старик не простой оказался, он потребовал за ключ шкуру жабы-электро-мага-с-посохом.")
                        print("Поэтому пришлось нашему магу вернуться к той жабе, да прикончить её.")
                        print("И вот, наш маг принес ему шкуру. Дед отдал ему ключ, маг пошёл к сундуку. Открыл он его, а там карта мира с реальным изображением всего на свете.")
                        print("(Существа ландшафт, погода и т.д) с возможностью приблизить картинку. Вышел он из пещерыда направился дальше.")
                        print()
                        print("Шёл он, шёл, по карте направлял себя и пришёл в огромный город магов под названием *Икатия*")
                        print("Ходил он по городу, докапывался до жителей, спрашивал, где тут можно найти какого-нибудь сильного мага, который помог бы ему")
                        print("познать свои силы, да стать таким же великим волшебником, как он.")
                        print("В итоге он всех кароче достал, за переулком его поймали, вырубили, связали крепко-накрепко, чтобы уж точно не выбрался")
                        print(", да отправили его кораблём на другой материк к чёртовой тёще. Но на этом его путешествие только начинается.")
                        print("Там он очнулся в клетке, сожрать его хотели, потому-что уж слишком он всех взбесил, людоедами  жители")
                        print("некоторые оказались. И вот, ждёт он уже своей учести, да нет, не получается у них употреблять его в пищу, потому-что")
                        print("прибывает на помощь флот Империи Нари, которая на материке этом правит. И вот, спасли они всех заключённых, доолго")
                        print("благодорил их маг, нашёл он там себе наставника, да вот наставник тоже не простой. Потребовал он с него работу-")
                        print("или работать, или вали обратно в дом свой родной. Предстал перед нашем магом выбор:")
                        print("[ВЫБОР] - (((1)работать) - помогать ему в хозяйстве или (2()свалить))")
                        way = int(input())
                        if way == 2:
                            print("Он вас убил. Смерть!")
                            print("Вы проиграли.")
                            exit
                        else:
                            print("И конечно же маг наш умный и выбрал работать на него, и обучаться. И вот спутся годы он познал всю магию. Поблагодарил он мага этого, да уехал к себе домой.")
                            print("Там он сдох в старости. Конец вы проиграли.")
                            exit
