# python3
# Vitalijs Vasiljevs 221RDB265 3.grupa
from collections import namedtuple
import re #Importēju moduli re, lai tiktu galā ar neparedzētu problēmu.

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = [] #Mainīju nosaukumu, lai būtu ērtāk.
    for i, next in enumerate(text): 
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1)) # Steku papildinu ar jaunu iekavu
            pass

        if next in ")]}":
            if len(opening_brackets_stack) > 0 :    # Pārbaudām, vai stekā ir iekavas
                last_bracket = opening_brackets_stack[-1]            # Atrod pēdējo ievadīto steka iekavu
                answer = are_matching(last_bracket.char, next)       # Pārbauda, vai pēdējā atvērtā iekava ir tāda pati kā jaunā aizvērtā iekava
                if (answer == False) : return i+1                    # Ja “answer” ir false, tad atgriež pēdējās aizvērtās iekavas atrašanās vietu
                opening_brackets_stack.pop()                         # Ja “answer” ir true, tad no steka izņem pēdējo ievadīto atvērto iekavu
            else: 
                return i+1                          #Ja stekā nav iekavu, tad atgriežam pēdējās aizvērtās iekavas atrašanās vietu
            pass
        
    if len(opening_brackets_stack) > 0: #Pārbauda, vai stekā pēc cikla ir palikušas iekavas
        return opening_brackets_stack[0].position #Atgriež pēdējās atvērtās iekavas atrašanās vietu
    else:
        return "Success"                #Ja steks ir tukšs, tad viss ir kārtībā un atgriež “Succes”

def main():
    mode = input()  #Lietotājs ievada burtu, lai izvēlētos režīmu
    if ((re.sub("[\r\n]", "", mode) == "I")) : ##pārbaudu, vai ierakstītais burts ir vienāds ar “I”. P. S. Atradu problēmu, ka tests ievada nevis I, bet I\r\n, tāpēc izmantoju sub funkciju, lai aizvietot \r\n ar tukšumu, lai nebūtu problēmu ar pārbaudi
        text = input()                              #Lietotājs ievada rindu ar simboliem un iekavām
        if len(text) > 10**5 : return               #Pārbaudu, vai ievadītās rindas garums nav pārsniedzis noteikto robežu 10^5
        mismatch = find_mismatch(text)              #Pārbaudu, vai nav kļūdas
        print(mismatch)                             #Izvadu atbildi

    elif (re.sub("[\r\n]", "", mode) == "F") :  #Nevarēju saprast, ko darīt tālāk
        return


if __name__ == "__main__":
    main()
