# python3
# Vitalijs Vasiljevs 221RDB265 3.grupa
from collections import namedtuple
import re #importeju moduli re, lai tikt gala ar neparedzetu problemu.

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = [] #mainīju nosaukumu, lai būtu ērtāk
    for i, next in enumerate(text): 
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1)) # 
            pass

        if next in ")]}":
            if len(opening_brackets_stack) > 0 :    # parbaudam vai steka ir iekavas
                last_bracket = opening_brackets_stack[-1]            # atrod pedejo ievaditu steka iekavu
                answer = are_matching(last_bracket.char, next)       # parbauda vai pedeja atverta iekava ir tada pasa ka jauna aizverta iekava
                if (answer == False) : return i+1                    # ja "answer" ir False, tad atgriezs pedejas aizvertas iekavas atrasanas vietu
                opening_brackets_stack.pop()                         # ja "answer" ir True, tad no steka iznem pedejo ievaditu atverto iekavu
            else: 
                return i+1                          #ja steka nav iekavu, tad atgriezam pedejas aizvertas iekavas atrasanas vietu
            pass
        
    if len(opening_brackets_stack) > 0: #parbauda vai steka pec cikla ir palikusas iekavas
        return opening_brackets_stack[0].position #atgriezs pedejas atvertas iekavas atrasanas vietu
    else:
        return "Success"                #ja steks ir tukss, tad viss ir kartiba un atgriezs "Succes"

def main():
    mode = input()  # lietotajs ievada burtu, lai izveleties rezimu
    if ((re.sub("[\r\n]", "", mode) == "I")) : #parbaudu vai ierakstits burts ir vienads ar "I".  P.S Atradu problemu, ka tests ievada nevis I, bet I\r\n, tapec izmantoju sub funkciju, lai aizvietot \r\n ar tuksumu, lai nebutu problemu ar parbaudi.
        text = input()                              #lietotajs ievada rindu ar simboliem un iekavam
        if len(text) > 10**5 : return               #parbaudu, vai ievaditas rindas garums nav parsniedzis noteiktu robezu 10^5
        mismatch = find_mismatch(text)              #parbaudu vai kludas
        print(mismatch)                             #izvadu atbildi

    elif (re.sub("[\r\n]", "", mode) == "F") :  #nevarēju saprast, ko darīt tālāk
        return


if __name__ == "__main__":
    main()
