#!/usr/bin/python
 
#importujemy tutaj wszystkie potrzebne rzeczy zeby program dzialal
import mysql.connector
import readline
from random import seed
from random import randint

#ustalamy parametry polaczenia oraz podajemy login i haslo do autoryzacji po czym laczymy sie z nia
hostname = 'localhost'
username = 'root'
password = 'ZrobmyPieczen1337'
database = 'pierwszy_program'
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
 
 
 
#zaczynamy od scenariusza pierwszego
scenario = 1
 
#definiujemy funkcje ktora pozwoli nam odczytac z bazy danych jakie potwory pojawiaja sie w tej scenie
def loadscenario( conn ):
 
    #podlaczany kursor oraz wywolujemy zapytanie do bazy danych dla okreslonego scenariusza
    cur0 = conn.cursor()
    cur0.execute( "SELECT * FROM scenarios WHERE stage_number=%d" % ( scenario ) )
 
    #rozpakowujemy zlepek danych do konkretnych miejsc w liscie monster_names
    for ( sn, sm1, sm2, sm3) in cur0.fetchall():
        stage_monster1 = sm1
        stage_monster2 = sm2
        stage_monster3 = sm3
        monster_names = [stage_monster1, stage_monster2, stage_monster3]
        return monster_names
 
#zle sformatowane dane wklejamy do listy zaczynajacej sie jako pusta potworek po potworku
monster_names = []
for name in loadscenario( myConnection ):
    monster_names.append(name)
 
 
#definiujemy funkcje ladowania pierwszego potworka w ktorej podlaczamy sie do bazy monsters
#oraz potem przypisujemy atrybuty zczytane z niej do klasy pierwszy potwor na ktorej bedziemy operowac w przyszlosci
def loadmonster1( conn ):
 
    #schemat podlaczenia sie oraz wykonania odpowiedniego zapytania pozwolacego pobrac nam dane
    cur1 = conn.cursor()
    sql1 = """SELECT monster_name, monster_AD, monster_HP, monster_abbility, monster_trait FROM monsters WHERE monster_name = %s"""
    first_monster = (monster_names[0], )
    cur1.execute(sql1, first_monster)
 
    #kolejny raz potrzebne jest formatowanie danych aby wszystko dzialalo plynnie przez wklejanie ich po kolei
    statistikz1 = []
    for stat in cur1.fetchall():
        statistikz1.append(stat)
 
        return statistikz1
 
#tak samo tutaj formatujemy nieprzyjemnie przeslane przez funkcje dane
statistikz1 = []
for stat in loadmonster1( myConnection ):
    statistikz1.append(stat)
 
#teraz definiujemy klase ktora bedzie posiadac zczytane atrybuty oraz umiejetnosci
for (mn1, mad1, mhp1, mab1, mat1) in statistikz1:
    class Monster1():
        def __init__(self):
            self.name = mn1
            self.AD = mad1
            self.HP = mhp1
            self.abbility = mab1
            self.trait = mat1
            self.turn = 1
 
        def attack(self, target):
            target.HP -= self.AD
            print("monster attacked for: %d")
 
 
 
 
#definiujemy funkcje ladowania pierwszego potworka w ktorej podlaczamy sie do bazy monsters
#oraz potem przypisujemy atrybuty zczytane z niej do klasy pierwszy potwor na ktorej bedziemy operowac w przyszlosci
def loadmonster2( conn ):
 
    #schemat podlaczenia sie oraz wykonania odpowiedniego zapytania pozwolacego pobrac nam dane
    cur2 = conn.cursor()
    sql2 = """SELECT monster_name, monster_AD, monster_HP, monster_abbility, monster_trait FROM monsters WHERE monster_name = %s"""
    second_monster = (monster_names[1],)
    cur2.execute(sql2, second_monster)
 
    #kolejny raz potrzebne jest formatowanie danych aby wszystko dzialalo plynnie przez wklejanie ich po kolei
    statistikz2 = []
    for stat in cur2.fetchall():
        statistikz2.append(stat)
 
        return statistikz2
 
 
#tak samo tutaj formatujemy nieprzyjemnie przeslane przez funkcje dane
statistikz2 = []
for stat in loadmonster2( myConnection ):
    statistikz2.append(stat)
 
#teraz definiujemy klase ktora bedzie posiadac zczytane atrybuty oraz umiejetnosci
for (mn2, mad2, mhp2, mab2, mat2) in statistikz2:
    class Monster2():
        def __init__(self):
            self.name = mn2
            self.AD = mad2
            self.HP = mhp2
            self.abbility = mab2
            self.trait = mat2
            self.turn = 1
 
        def attack(self, target):
            target.HP -= self.AD
            print("monster attacked for: %d")
 
#definiujemy funkcje ladowania pierwszego potworka w ktorej podlaczamy sie do bazy monsters
#oraz potem przypisujemy atrybuty zczytane z niej do klasy pierwszy potwor na ktorej bedziemy operowac w przyszlosci
def loadmonster3( conn ):
 
    #schemat podlaczenia sie oraz wykonania odpowiedniego zapytania pozwolacego pobrac nam dane
    cur3 = conn.cursor()
    sql3 = """SELECT monster_name, monster_AD, monster_HP, monster_abbility, monster_trait FROM monsters WHERE monster_name = %s"""
    third_monster = (monster_names[2],)
    cur3.execute(sql3, third_monster)
 
    #kolejny raz potrzebne jest formatowanie danych aby wszystko dzialalo plynnie przez wklejanie ich po kolei
    statistikz3 = []
    for stat in cur3.fetchall():
        statistikz3.append(stat)
 
        return statistikz3
 
#tak samo tutaj formatujemy nieprzyjemnie przeslane przez funkcje dane
statistikz3 = []
for stat in loadmonster3( myConnection ):
    statistikz3.append(stat)
 
#teraz definiujemy klase ktora bedzie posiadac zczytane atrybuty oraz umiejetnosci
for (mn3, mad3, mhp3, mab3, mat3) in statistikz3:
    class Monster3():
        def __init__(self):
            self.name = mn3
            self.AD = mad3
            self.HP = mhp3
            self.abbility = mab3
            self.trait = mat3
            self.turn = 1
 
        def attack(self, target):
            target.HP -= self.AD
            print("monster attacked for: %d")
 
 
#tworzymy instancje czyli jednostki potworow z danej klasy kolejnosciowej
first_enemy = Monster1()
second_enemy = Monster2()
third_enemy = Monster3()


#tutaj tworzymy tabele ktore pomoga nam w iteracji kodu
monster_table = [first_enemy, second_enemy, third_enemy]
monsters_with_HP = [first_enemy, second_enemy, third_enemy]
hero_table = []
 
 
#tutaj pobieramy czary tak aby zaladowane mogly zostac obsluzone w grze
def load_spells(conn):
    cur5 = conn.cursor()
    sql5 ="""SELECT * FROM abbilities"""
    cur5.execute(sql5)
 
    spells = []
    for spell in cur5.fetchall():
        spells.append(spell)
 
    return spells
 
#tworzymy tutaj slownik ktory po nazwie czaru bedzie zwracal jego statystyki aby mozna bylo ich uzyc dalej
spells = {}
for sn, group, target, power in load_spells( myConnection ):
    spells[sn] = (group, target, power)

#definiujemy funkcje ktora bedzie wykozystywana przez bohaterow do zadawania obrazen podstawowych
def melee_attack(attack_damage):
    print("what monster you wish to attack:")

#tutaj wypisujemy potwory ktore mozna zaatakowac
    j = 1
    while j <= len(monsters_with_HP):
        print( "%d to attack: %s" % ( j, (monsters_with_HP[j-1]).name ) )
        j += 1

#tutaj pobieramy od uzytkownika jakiego potwora chce zaatakowac oraz wykonujemy atak
    while True:
        try:
            selected_monster = input("type number:")
            ( monster_table[ int( selected_monster ) - 1 ] ).HP -= attack_damage
            break

# w wypadku gdyby mial nastapic blad w programie spowodowany niepoprawnymi danymi program obsluguje wyjatki
        except(ValueError):
            print("that was not valid number")

        except IndexError:
            print("please use numbers from 1 to 3")


# tutaj definiujemy funkcje ktora bedzie uzywana do rzucania zaklec
def casting_spell(spell_type):


#wybieramy zaklecie i przypisujemy je do zmiennej z tabeli zaklec
    spell = spells[spell_type]

#jezeli zaklecie atakuje pojedynczego wroga pytamy kogo uzytkownik chce zaatakowac
    if spell[0] == "enemy":
        print("what monster you wish to attack:")
        print("1:%s, 2:%s, 3:%s" % ( ( monster_table[0]).name, (monster_table[1]).name, (monster_table[2]).name ) )
        while True:

#pobieramy od uzytkownika liczbe ktora jest sprawdzana pod katem wyjatkow oraz czar jest badany pod katem tego gdzie mierzy we wroga
            try:
                selected_monster = input("type number:")
                if spell[1] == "turn":
                    ( monster_table[ int(selected_monster) - 1] ).turn = 0
                    ( monster_table[ int(selected_monster) - 1] ).HP -= spell[2]
                    break

                if spell[1] == "AD":
                    ( monster_table[ int(selected_monster) - 1] ).AD -= spell[2]
                    break

                if spell[1] == "HP":
                    ( monster_table[ int(selected_monster) - 1] ).HP -= spell[2]
                    break

#obslugujemy wyjatki w razie niepoprawneych danych od uzytkownika
            except(ValueError):
                print("that was not valid number")

            except IndexError:
                print("please use numbers from 1 to 3")


#w wypadku gdyby atakowal wszystkich wrogow to zmniejszamy im zycie odpowiednio
    if spell[0] == "enemies":
        (monster_table[0]).HP -= spell[2]
        (monster_table[1]).HP -= spell[2]
        (monster_table[2]).HP -= spell[2]


#gdy czar ma wspomoc bohatera to sprawdzamy jakiego chce on wspomoc
    if spell[0] == "hero":
        print("what hero would you assist")
        print( "1:%s, 2:%s, 3:%s" % ( ( (hero_table[0]).name, (hero_table[1]).name, (hero_table[2]).name) ) )
        while True:

#gdy odczytujemy jakiego bohatera to po chwili po sprawdzeniu w jaki sposob mamy go wspomoc wykonujemy to wszystko
            try:
                selected_hero = input("type number:")

                if spell[1] == "AD":
                    (hero_table[ int(selected_hero) - 1] ).AD += spell[2]
                    break

                if spell[1] == "HP":
                    (hero_table[ int(selected_hero) - 1]).HP += spell[2]
                    break


# w razie wystapienia wyjatku jest on obslugiwany odpowiednio
            except(ValueError):
                print("that was not valid number")

            except IndexError:
                print("please use numbers from 1 to 3")


#gdy czar leczy wszystkich bohaterow to zwiekszamy im zycie odpowiednio
    if spell[0] == "heroes":
        (hero_table[0]).HP += spell[2]
        (hero_table[1]).HP += spell[2]
        (hero_table[2]).HP += spell[2]

#laczymy sie z baza danych aby podbrac dane pierwszego bohatera
def load_hero1(conn):
    cur4 = conn.cursor()
    sql4 = """SELECT hero_name, hero_AD, hero_HP, hero_spell_1, hero_spell_2, hero_spell_3 FROM heroes WHERE hero_name = 'Roy'  """
    cur4.execute(sql4)
 
    # kolejny raz potrzebne jest formatowanie danych aby wszystko dzialalo plynnie przez wklejanie ich po kolei
    statistikz4 = []
    for stat in cur4.fetchall():
        statistikz4.append(stat)
 
        return statistikz4
 

 
# tak samo tutaj formatujemy nieprzyjemnie przeslane przez funkcje dane
statistikz4 = []
for stat in load_hero1(myConnection):
    statistikz4.append(stat)
 

#dzieki pobranym danym ustalamy statystyki bohatera na stan poczatkowy
for (hn1, had1, hhp1, hs11, hs12, hs13) in statistikz4:
    class Hero1():
        def __init__(self):
            self.name = hn1
            self.AD = had1
            self.HP = hhp1
            self.spell_1 = hs11
            self.spell_2 = hs12
            self.spell_3 = hs13
            self.turn = 1
 
#nadajemy metode ataku bohaterowi dzieki pomocniczej funkcji nie trzeba pisac az tyle kodu oraz zerujemy jego ture po skonczonym ataku
        def attack(self):
            melee_attack(self.AD)
            self.turn = 0
 
 #nadajemy metode ataku czarem dzieki pomocniczej funkkcji jest to prostrze
        def cast(self):

#pytamy uzytkownika jakiego czaru chce uzyc pobierajac jego czarny i wypisujac je
            print("what attack you do wish to perform")
            print("1:%s, 2:%s, 3:%s" % ( self.spell_1, self.spell_2, self.spell_3 ) )

#uzyskujemy od uzytkownika liczbe ktora ma nam posluzyc aby wiedziec jaki czar chce wykonac
            while True:
                try:
                    selected_spell =  input("type number:")
                    selected_spell = int(selected_spell)

#jezeli nie wpisal liczby petla jest powtarzana do momentu uzyskania poprawnych danych
                except ValueError:
                    print("invalid input please use numbers")

#przypisujemy odpowiedni czar do zmiennej aby mogl on funkcjonowac dalej
                if selected_spell == 1:
                    spell_name = self.spell_1
                    break

                if selected_spell == 2:
                    spell_name = self.spell_2
                    break

                if selected_spell == 3:
                    spell_name = self.spell_3
                    break

                else:
                    print("invalid number please use from 1 to 3")

#rzucamy czar za pomoca wczesniejszej funkcji
            casting_spell(spell_name)

            self.turn = 0
 

                            

def load_hero2(conn):
    cur5 = conn.cursor()
    sql5 = """SELECT hero_name, hero_AD, hero_HP, hero_spell_1, hero_spell_2, hero_spell_3 FROM heroes WHERE hero_name = 'Michaella'  """
    cur5.execute(sql5)
 
    # kolejny raz potrzebne jest formatowanie danych aby wszystko dzialalo plynnie przez wklejanie ich po kolei
    statistikz5 = []
    for stat in cur5.fetchall():
        statistikz5.append(stat)
 
        return statistikz5
 
 
# tak samo tutaj formatujemy nieprzyjemnie przeslane przez funkcje dane
statistikz5 = []
for stat in load_hero2( myConnection ):
    statistikz5.append(stat)
 
for (hn2, had2, hhp2, hs21, hs22, hs23) in statistikz5:
    class Hero2():
        def __init__(self):
            self.name = hn2
            self.AD = had2
            self.HP = hhp2
            self.spell_1 = hs21
            self.spell_2 = hs22
            self.spell_3 = hs23
            self.turn = 1
 
#nadajemy metode ataku bohaterowi dzieki pomocniczej funkcji nie trzeba pisac az tyle kodu oraz zerujemy jego ture po skonczonym ataku
        def attack(self):
            melee_attack(self.AD)
            self.turn = 0
 
 #nadajemy metode ataku czarem dzieki pomocniczej funkkcji jest to prostrze
        def cast(self):

#pytamy uzytkownika jakiego czaru chce uzyc pobierajac jego czarny i wypisujac je
            print("what attack you do wish to perform")
            print("1:%s, 2:%s, 3:%s" % ( self.spell_1, self.spell_2, self.spell_3 ) )

#uzyskujemy od uzytkownika liczbe ktora ma nam posluzyc aby wiedziec jaki czar chce wykonac
            while True:
                try:
                    selected_spell =  input("type number:")
                    selected_spell = int(selected_spell)

#jezeli nie wpisal liczby petla jest powtarzana do momentu uzyskania poprawnych danych
                except ValueError:
                    print("invalid input please use numbers")

#przypisujemy odpowiedni czar do zmiennej aby mogl on funkcjonowac dalej
                if selected_spell == 1:
                    spell_name = self.spell_1
                    break

                if selected_spell == 2:
                    spell_name = self.spell_2
                    break

                if selected_spell == 3:
                    spell_name = self.spell_3
                    break

                else:
                    print("invalid number please use from 1 to 3")

#rzucamy czar za pomoca wczesniejszej funkcji
            casting_spell(spell_name)

            self.turn = 0
 
                            
 
def load_hero3(conn):
    cur6 = conn.cursor()
    sql6 = """SELECT hero_name, hero_AD, hero_HP, hero_spell_1, hero_spell_2, hero_spell_3 FROM heroes WHERE hero_name = 'Tanya'  """
    cur6.execute(sql6)
 
    # kolejny raz potrzebne jest formatowanie danych aby wszystko dzialalo plynnie przez wklejanie ich po kolei
    statistikz6 = []
    for stat in cur6.fetchall():
        statistikz6.append(stat)
 
        return statistikz6
 
 
# tak samo tutaj formatujemy nieprzyjemnie przeslane przez funkcje dane
statistikz6 = []
for stat in load_hero3( myConnection ):
    statistikz6.append(stat)
 
for (hn3, had3, hhp3, hs31, hs32, hs33) in statistikz6:
    class Hero3():
        def __init__(self):
            self.name = hn3
            self.AD = had3
            self.HP = hhp3
            self.spell_1 = hs31
            self.spell_2 = hs32
            self.spell_3 = hs33
            self.turn = 1

#nadajemy metode ataku bohaterowi dzieki pomocniczej funkcji nie trzeba pisac az tyle kodu oraz zerujemy jego ture po skonczonym ataku
        def attack(self):
            melee_attack(self.AD)
            self.turn = 0
 
 #nadajemy metode ataku czarem dzieki pomocniczej funkkcji jest to prostrze
        def cast(self):

#pytamy uzytkownika jakiego czaru chce uzyc pobierajac jego czarny i wypisujac je
            print("what attack you do wish to perform")
            print("1:%s, 2:%s, 3:%s" % ( self.spell_1, self.spell_2, self.spell_3 ) )

#uzyskujemy od uzytkownika liczbe ktora ma nam posluzyc aby wiedziec jaki czar chce wykonac
            while True:
                try:
                    selected_spell =  input("type number:")
                    selected_spell = int(selected_spell)

#jezeli nie wpisal liczby petla jest powtarzana do momentu uzyskania poprawnych danych
                except ValueError:
                    print("invalid input please use numbers")

#przypisujemy odpowiedni czar do zmiennej aby mogl on funkcjonowac dalej
                if selected_spell == 1:
                    spell_name = self.spell_1
                    break

                if selected_spell == 2:
                    spell_name = self.spell_2
                    break

                if selected_spell == 3:
                    spell_name = self.spell_3
                    break

                else:
                    print("invalid number please use from 1 to 3")

#rzucamy czar za pomoca wczesniejszej funkcji
            casting_spell(spell_name)

            self.turn = 0
 

#tworzymy instancje ktore pomozwola nam poprowadzic walke
first_hero = Hero1()
second_hero = Hero2()
third_hero = Hero3()

#tutaj na razie rozlaczamy sie z baza danych w skonczonej wersji bedzie to pozniej
myConnection.close()


#ladujemy kazdego z bohaterow do tabeli dla wlasnej wygody wykonywania programu
hero_table.append(first_hero)
hero_table.append(second_hero)
hero_table.append(third_hero)

#definiujemy funkcje wyswietlajaca bohateow ktorzy maja jeszcze ture
def list_movable_heroes():
    movable_heroes = []

#jezeli bohater ma jeszcze ture to zostanie on dolaczony do tabeli
    if  ( (hero_table[0]).turn == 1):
        movable_heroes.append( (hero_table[0]) )

    if ( (hero_table[1]).turn == 1):
        movable_heroes.append( (hero_table[1]) )

    if ( (hero_table[2]).turn == 1): 
        movable_heroes.append( (hero_table[2]) )

#tutaj wypisujemy wszystkich bohaterow z tabeli
    print("You can move with those heroes:")
    i = 0
    while i <= (len(movable_heroes)-1):
        print( "%d:%s" % ( (i+1), (movable_heroes[i]).name ) )
        i += 1

#zwracamy tabele z bohaterami posiadajacymi jeszcze ruch
    return movable_heroes


#az do momentu w ktorym wygramy prowadzona bedzie walka
win = False
while win == False:

#wypisujemy HP wszystkich ktorzy sa na mapie aby bylo widac jak wyglada sytuacja po kazdym ruchu
    while True:
        print("1st hero HP: %d, 2nd hero HP: %d, 3rd hero HP: %d" % ( (hero_table[0]).HP, (hero_table[1]).HP, (hero_table[2]).HP ) )
        print("%s HP: %d, %s HP: %d, %s HP: %d" % ( (monster_table[0]).name, (monster_table[0]).HP, (monster_table[1]).name, (monster_table[1]).HP, (monster_table[2]).name, (monster_table[2]).HP, ) )

        HWM = []
        for heroes_with_move in list_movable_heroes():
            HWM.append(heroes_with_move)

 
        while True:

#pobieramy od uzytkownika jakim bohaterem chce sie poruszyc 
            try:
                hero_to_move_number = input("what hero you wish to move: you can choose from 1 to %d: " % (len(HWM)))
                hero_to_move = HWM[ int(hero_to_move_number) - 1]

#w wypadku niepoprawnych danych wyjatki sa obslugiwane
            except(ValueError):
                print("that was not valid number")


            except IndexError:
                print("please use numbers from 1 to 3")

#pytamy sie go teraz czy chce uzyc podstawowego ataku czy rzucic zaklecie
            try: 
                action = input("type 1 to attack and 2 to cast: ")
                action = int(action)

#ponownie wyjatek jest obsluiwany
            except(ValueError):
                print("that was not valid number")

            finally:

#wykonujemy akcje ktora wybral sobie uzytkownik
                if action == 1:
                    (hero_to_move).attack()
                    break

                if action == 2:
                    (hero_to_move).cast()
                    break
                
                else:
                    print("please use numbers from 1 to 2")



#jezeli wszystkie potwory sa niezywe uzytkownik wygrywa i w pozniejszych wersjach przechodzi do nastepnego etapu
        if ( (monster_table[0]).HP <= 0 ) and ( (monster_table[1]).HP <= 0 ) and ( (monster_table[2]).HP <= 0 ):
            win = True
            print("congratulations you have won")
            break

        if len(HWM) <= 1:
            break

#dla kazdego potwora ktory jest zywy wykonujemy akcje ataku na losowego bohatera
    for monster_that_attacks in monster_table:

        if (monster_that_attacks).HP > 0:
            (monster_that_attacks).attack( hero_table[ randint(0, 2) ] )

#odnawiamy ture bohaterom aby ci mogli walczyc w nastepnej turze
    (hero_table[0]).turn = 1
    (hero_table[1]).turn = 1
    (hero_table[2]).turn = 1
