from abc import ABC, abstractmethod
import re
import math
import numpy as np
import datetime
import random
import sys
sys.path.insert(0,"other_projects")
import exchange, verb_segmentator, taylor_swift, chohan, dz3

def log_print(message_to_print, log_file=f"log_files\\output_{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"):
    try:
        print(message_to_print)
        with open(log_file, 'a') as of:
            of.write(message_to_print + '\n')
    except UnicodeEncodeError:
        pass

class ProblemStrategy(ABC):
    @abstractmethod
    def solve(self, input):
        pass

class MathProblem1(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You: ")
            points = re.findall("(\d+\.?\d?)",input1)
            if len(points)==6:
                log_print(f"Розум'ян: {math.sqrt(((float(points[3])-float(points[0]))**2)+((float(points[4])-float(points[1]))**2)+((float(points[5])-float(points[2]))**2))}")
                result = True
            elif input1=="Назад":
                result = True
            else:
                log_print("Розум'ян: Не зрозумів ваш запит, спробуйте ще раз")

class MathProblem2(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You1: ")
            if input1=="1":
                log_print("Розум'ян: Гаразд, вкажи довжину сторони трикутникa та довжину висоти, проведеної до неї (я вважатиму, що виміру йдуть в сантиметрах)")
                input1 = input("You1: ")
                lengths = re.findall("(\d+\.?\d?)", input1)
                if len(lengths) == 2:
                    log_print(f"Розум'ян: {float(lengths[0])*float(lengths[1])} см^2")
                    result = True
            elif input1 == "2":
                log_print("Розум'ян: Гаразд, вкажи дві сторони у форматі векторів (я вважатиму, що виміру йдуть в сантиметрах)")
                input1 = input("You1: ")
                lengths = re.findall("(\d+\.?\d?)", input1)
                if len(lengths) == 6:
                    vector1 = np.array([float(i) for i in lengths[:3]])
                    vector2 = np.array([float(i) for i in lengths[3:]])
                    log_print(f"Розум'ян: {np.linalg.norm(np.cross(vector1,vector2),ord=2)*0.5} см^2")
                    result = True
            elif input1=="Назад":
                result = True
            else:
                log_print("Розум'ян: Не зрозумів ваш запит, спробуйте ще раз")

class WorkWithTextProblem1(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You1: ")
            number_words = re.findall("\b(\d+\.?\d?)\b",input1)
            if len(number_words) > 0:
                log_print(f"Розум'ян: {number_words}")
                result = True
            elif input1=="Назад":
                result = True
            else:
                log_print("Розум'ян: Не знайшов жодного такого слова:(")

class WorkWithTextProblem2(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You1: ")
            latin_words = re.findall("[a-zA-Z]+",input1)
            if len(latin_words) > 0:
                log_print(f"Розум'ян: {latin_words}")
                result = True
            elif input1=="Назад":
                result = True
            else:
                log_print("Розум'ян: Не знайшов жодного такого слова:(")

class WorkWithTextProblem3(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You1: ")
            no_spaces = re.sub("\s{2,}"," ",input1)
            if input1 != no_spaces:
                log_print(f"Розум'ян: {no_spaces}")
                result = True
            elif input1=="Назад":
                result = True
            else:
                log_print("Розум'ян: Твій текст і так в порядку)")

class WorkWithTextProblem4(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You1: ")
            sentences = input1.split(". ")
            if len(sentences) > 0:
                tokenized_sentences = [sentence.split(" ") for sentence in sentences]
                longest_sen = max(tokenized_sentences, key=len)
                longest_sen_len = len(longest_sen)
                log_print(f"Розум'ян: Найдовше речення «{' '.join(longest_sen)}», складається з {longest_sen_len} слів")
                result = True
            elif input1 == "Назад":
                result = True
            else:
                log_print("Розум'ян: Порожньо..?")

class WorkWithTextProblem5(ProblemStrategy):
    def solve(self):
        result = False
        while not result:
            input1 = input("You1: ")
            string = [*input1.lower()]
            if len(string) > 0:
                count = [(i, string.count(i)) for i in set(string)]
                log_print(f"Розум'ян: Найчастіше трапляється символ «{max(count, key=lambda x: x[1])[0]}», кількість разів: {max(count, key=lambda x: x[1])[1]}")
                result = True
            elif input1 == "Назад":
                result = True
            else:
                log_print("Розум'ян: Порожньо..?")

class MiscellaneousProblem1(ProblemStrategy):
    def solve(self):
        x = datetime.datetime.now()
        log_print(f"Розум'ян: Зараз {x.strftime('%m')} місяць {x.strftime('%Y')} року.")

class MiscellaneousProblem2(ProblemStrategy):
    def solve(self):
        story_male = [
            "Був собі хлопчик {character_name}. Мав тата і маму, старшого брата Івася і стареньку бабусю. Тато ходив на роботу, брат учився в школі, а мама і бабуся залишалися вдома з Сергійком.\nВесь день вони тільки й знали, що ходили слідом за {character_name}.\n— Сергійку, йди борщ їсти!\n— Не хо-очу, він ки-ислий!\n— {character_name}, на молока випий!\n— Не хо-очу, воно бі-іле!\n— {character_name}, трохи медку з’їж!\n— Не хо-очу, він солодкий!\nТільки й чули від нього оте: «Не хочу!» Що мама не купувала, що бабуся не пекла та не варила — все {character_name} не так. ",
            "Гу-гу-гу!.. Ого-го!.. Ха-ха-ха!.. — залунало по лісі тихої літньої ночі.\nДві подорожні баби, що йшли на прощу й запізнилися завидна дійти до села, злякано перехрестились, їм стало моторошно, хоча вони й гадали, що то закричав пугач.\nАле ж всі лісові створіння добре знали, що то гукає {character_name}, який кожної п’ятниці прибігав у ліс з сусіднього великого болота, щоб трохи побавитися в гурті іншої Невидимої Сили. Любив він пожартувати, посміятися, злякати людину чи поглузувати з неї.\nКоли ж починав оповідати, то всі тільки головами крутили. А старий статечний Лісовик, що увесь час нюхав замість тютюну порохню, потихеньку нахилявся до свого товариша Водяника, непомітно підморгував сивою бровою й примовляв:\n— Слухай, слухай! Бреше Бісів син, мов шовком шиє!..\nВодяник задоволено кректав, як жаба-ропуха, спльовував через губу й смоктав далі свою люлечку з очеретяним цибухом.\nА тим часом {character_name} дуже мало брехав. Був він тільки великий хвалько, за що його батько Біс розгнівався на нього й послав у болото. Але ж перед тим {character_name} багато бачив на своєму віку. Ви ж бо самі знаєте, що Дідько ніколи не сидить довго на одному місці, а через якийсь час має призначення кудись-інде, де й змінює своє наймення.",
            "Один скромний підмайстер на ім’я {character_name} навчався ремесла у вправного кравця.\nБувало, що він годинами шив без перепочинку, а іноді – і траплялося це часто – він сидів, глибоко замислившись, дивлячись в одну точку.\n– {character_name} знову прибрав вигляду вельможної особи, – казали тоді про нього кравець та інші підмайстри.\nА по п’ятницях, коли люди спокійно йшли з молитви, {character_name} виходив із мечеті у святковому одязі й повільно крокував містом, велично киваючи знайомим. І коли кравець казав йому жартома: «У тобі пропадає принц, {character_name}», він дуже радів і відповідав: «Я вже давно про це думав!»\nАж кравець мирився з такою поведінкою, бо {character_name} був загалом гарною людиною та майстерним робітником."]
        story_female = [
            "Такого імені, як {character_name}, ніколи раніше в Персії і не чули. Але справа в тому, що мати принцеси була родом з далекої Півночі. У молодості вона потрапила в полон до африканського пірата і врешті-решт, завдяки незрівнянній красі, була продана до гарему перського шаха. Він підніс її, зробивши своєю дружиною, і любив набагато більше всіх інших дружин. Прекрасна шахиня, яка вже померла, назвала свою єдину дочку {character_name}, що означає «Липа золота».\nЦим ім’ям шахиня хотіла сказати, що принцеса так само чиста і прекрасна, як сонце, чиї золоті промені грають навесні серед листя чудесних лип півночі.\nПринцеса {character_name} успадкувала царську поставу батька, а фігуру і риси обличчя – матері. Серце її було благородне і ніжне. І тому в усій великій державі Шах Надира не було нікого, хто б не любив її.",
            "Cердитий осінній вітер віяв на Крезькому плоскогір’ї. Сутеніло. Стомлена маленька {character_name} поверталася зі школи; у неї боліли ніжки. Воно й не диво: багато бігала на перервах, та й школа була від її домівки аж за п’ять кілометрів. П’ять кілометрів туди та назад… Це далека дорога, навіть коли не стомлені ноги.\nХотілося трохи спочити, але зупинятися не можна — мама заборонила. І в глибину лісу також не можна заходити. Дівчинка йшла широкою стежкою, по якій у базарні дні проїздили возами.\nКажуть, вовки не виходять на стежку. Хіба що дуже вже зголодніють.\nПростуючи лісом, {character_name} щоразу згадувала про вовків: чи не дуже вони голодні? Якось вона таки зустріла одного, але подумала, що то великий собака, і не злякалася, хоч у нього й світилися очі. Вовк якийсь час ішов слідом, а потім зник у лісі.\nДома {character_name} розповіла про свою пригоду. Після того трохи не місяць мама проводжала її майже до самої школи, а ввечері тато робив так, щоб забрати {character_name} із собою. Однак завжди так не могло бути, бо в мами багато клопоту ще з трьома дітьми — двома меншими братиками і старшою хворою сестричкою, А тато, працюючи на сусідніх фермерів, надвечір ледве ноги носив.\nМусила дівчинка знову сама ходити до школи.",
            "Удрімучому лісі жила стара {character_name}. Якось раз їй дуже захотілося поласувати яйцями інших птахів, і вона придумала хитрість.\n{character_name} підлетіла до пташиних гнізд, спустилася на землю, встала під деревом на одну ногу і розкрила свій дзьоб.\nПтахи побачили {character_name} і дуже здивувалися, чому вона так стоїть.\n– Шановна, хто ви така? – запитала одна птах.\n– Я – відлюдниця – відповіла {character_name}.\nТоді птахи запитали:\n– А чому ви стоїте на одній нозі?\n– О, – сказала {character_name}, – дуже я важка! Якщо поставлю на землю другу ногу, то земля від такої тяжкості впаде.\n– А чому у вас дзьоб розкритий?\n– Тому, що я харчуюся тільки повітрям і більше нічого не їм, – з гордістю відповіла {character_name}.\n– Так, – вирішили птахи, – ця ворона дійсно цнотлива відлюдниця. Чому б нам не попросити її посторожувати наші гнізда з яйцями?"]
        result = False
        while not result:
            log_print(f"Розум'ян: Тож, як зватимуть героя?")
            character = input("You1: ")
            log_print(f"Розум'ян: Якої статі цей персонаж? (ч - чоловіча, ж - жіноча)")
            character_sex = input("You1: ")
            if character_sex == 'ч':
                log_print(f"Розум'ян: {random.choice(story_male)}".format(character_name = character))
            elif character_sex == 'ж':
                log_print(f"Розум'ян: {random.choice(story_female)}".format(character_name = character))
            elif character == "Назад" or character_sex == "Назад":
                result = True
            else:
                log_print("Розум'ян: Ти щось наплутав, давай заново")

class Other_CurrencyExchange(ProblemStrategy):
    def solve(self):
        exchange.CurrencyExchange()

class Other_VerbSegmentator(ProblemStrategy):
    def solve(self):
        verb_segmentator.VerbSegmentator()

class Other_TaylorSwift(ProblemStrategy):
    def solve(self):
        taylor_swift.TaylorSwift()

class Other_ChoHan(ProblemStrategy):
    def solve(self):
        chohan.ChoHan()

class Other_Coin(ProblemStrategy):
    def solve(self):
        dz3.CoinCount()

class Text(ProblemStrategy):
    def solve(self):
        return None

def Solver(strategy):
    strategies = {
        "mathematics/distance between two points": MathProblem1,
        "mathematics/triangle's area": MathProblem2,
        "work with text/search number words": WorkWithTextProblem1,
        "work with text/search latin script words": WorkWithTextProblem2,
        "work with text/delete extra spaces": WorkWithTextProblem3,
        "work with text/longest sentence": WorkWithTextProblem4,
        "work with text/most frequent letter": WorkWithTextProblem5,
        "miscellaneous/year and month": MiscellaneousProblem1,
        "miscellaneous/story" : MiscellaneousProblem2,
        "other projects/currency" : Other_CurrencyExchange,
        "other projects/verb segmentator":Other_VerbSegmentator,
        "other projects/taylor swift":Other_TaylorSwift,
        "other projects/cho-han":Other_ChoHan,
        "other projects/coin":Other_Coin

    }
    if strategy in strategies:
        return strategies[strategy]()
    else:
        return Text()
