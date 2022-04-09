import requests
from bs4 import BeautifulSoup

#Bring back the words from one url
def get_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    words_raw = soup.find_all("li")

    word_all = []
    for element in words_raw:
        word_all.append(element.string)

    return word_all


#create a list with all the urls
def list_creator():

    first_letter = input("First letter ?  ")
    lst = []

    for i in range(0,9):
        a = f"https://www.le-dictionnaire.com/repertoire/{first_letter}0{i}.html"
        lst.append(a)
    for i in range(10,27):
        a = f"https://www.le-dictionnaire.com/repertoire/{first_letter}{i}.html"
        lst.append(a)

    return lst

#Bring back all the words from all the urls created with the 2 others functions
def getter():
    bordel = []
    lst = list_creator()
    for element in lst:
        for z in get_url(element):
            bordel.append(str(z))

    return bordel


#Create 1 list with letter and place (accents are taken into acount, French version)
def letter_place_selector():
    ltr_place = []

    while True :
        ltr = input("Letter ?  ")
        place = input("place of this letter?  ")

        ltr_place.extend(ltr)
        ltr_place.extend(place)

        cont = input("another letter ? (y/n)  ")
        if cont.lower() == "n":
            for i,element in enumerate(ltr_place):
                if element.isdigit():
                    ltr_place[i] = int(element)
            break

        if cont.lower() == "y":
            continue

    return ltr_place



def debroussailleur():
    all_words = getter()
    good_ones = []
    almost_ones = []
    bad_ones = []
    length = int(input("length of the word ? (in digits)  "))

    while True:
        final_words = []
        final_words2 = []
        final_words3 = []

        print("This section is about the letter at the GOOD place : ")
        good_ones.extend(letter_place_selector())
        print("This section is about the letter at the WRONG place : ")
        almost_ones.extend(letter_place_selector())
        print("This section is about the letter not present in the word : ")
        bad_ones.extend(letter_place_selector())

        #Good_ones part :
        if good_ones == []:
            final_words.extend(all_words)
        else:
            for element4 in all_words :
                for i in range(0, len(good_ones), 2):
                    if len(element4) == length:

                        if good_ones[i] == "e" :
                            if "e"  == element4[good_ones[i + 1]] or "é" == element4[good_ones[i + 1]] or "ê"  == element4[good_ones[i + 1]] or "è"  == element4[good_ones[i + 1]] :
                                if all(good_ones[k] == element4[good_ones[k + 1]] for k in range(0, i, 2)) == True :
                                    if all(good_ones[l] == element4[good_ones[l + 1]] for l in range(i + 2, len(good_ones), 2)) == True :
                                        if element4 not in final_words:
                                            final_words.append(element4)
                        
                        elif good_ones[i] == "a" :
                            if "a"  == element4[good_ones[i + 1]] or "â" == element4[good_ones[i + 1]] :
                                if all(good_ones[k] == element4[good_ones[k + 1]] for k in range(0, i, 2)) == True :
                                    if all(good_ones[l] == element4[good_ones[l + 1]] for l in range(i + 2, len(good_ones), 2)) == True :
                                        if element4 not in final_words:       
                                            final_words.append(element4)

                        else : 
                            if all(good_ones[j] == element4[good_ones[j + 1]] for j in range(0, len(good_ones), 2)) == True :
                                if element4 not in final_words:
                                    final_words.append(element4)

        #Almost_ones part : 
        if almost_ones == []:
            final_words2.extend(final_words)
        else:      
            for element4 in final_words :
                for i in range(0, len(almost_ones), 2):
                    if len(element4) == length:

                        if almost_ones[i] == "e":
                            if "e"  in element4 or "é" in element4 or "ê" in element4 or "è" in element4 :
                                if "e"  != element4[almost_ones[i + 1]] and "é" != element4[almost_ones[i + 1]] and "ê"  != element4[almost_ones[i + 1]] and "è"  != element4[almost_ones[i + 1]] :
                                    if all(almost_ones[j] != element4[almost_ones[j + 1]] for j in range(0, len(almost_ones), 2)) == True :
                                        if all(almost_ones[j] in element4 for j in range(0, len(almost_ones), 2)) == True :
                                            if element4 not in final_words2:
                                                final_words2.append(element4)

                        elif almost_ones[i] == "a":
                            if "a"  in element4 or "à" in element4 :
                                if "a"  != element4[almost_ones[i + 1]] and "à" != element4[almost_ones[i + 1]] :
                                    if all(almost_ones[j] != element4[almost_ones[j + 1]] for j in range(0, len(almost_ones), 2)) == True :
                                        if all(almost_ones[j] in element4 for j in range(0, len(almost_ones), 2)) == True :
                                            if element4 not in final_words2:
                                                final_words2.append(element4)

                        else : 
                            if all(almost_ones[j] != element4[almost_ones[j + 1]] for j in range(0, len(almost_ones), 2)) == True :
                                if all(almost_ones[j] in element4 for j in range(0, len(almost_ones), 2)) == True :
                                    if element4 not in final_words2:
                                        final_words2.append(element4)


        #Bad_ones:
        if good_ones == []:
            final_words3.extend(final_words2)
        else:
            for element4 in final_words2 :
                for i in range(0, len(bad_ones), 2):
                    if len(element4) == length:

                        if bad_ones[i] == "e":
                            if "e"  not in element4 and "é" not in element4 and "ê" not in element4 and not "è" in element4 :
                                if all(bad_ones[j] not in element4[bad_ones[j + 1]] for j in range(0, len(bad_ones), 2)) == True :
                                    if element4 not in final_words3:
                                        final_words3.append(element4)

                        if bad_ones[i] == "e":
                            if "e"  not in element4 and "à" not in element4 :
                                if all(bad_ones[j] not in element4 for j in range(0, len(bad_ones), 2)) == True :
                                    if element4 not in final_words3:
                                        final_words3.append(element4)

                        else :
                            if all(bad_ones[j] not in element4 for j in range(0, len(bad_ones), 2)) == True :
                                    if element4 not in final_words3:
                                        final_words3.append(element4) 


        print(final_words3)

        cont2 = input("Another word ? (y/n)  ")
        if cont2 == "y" : continue
        elif cont2 == "n" : break

    return

debroussailleur()