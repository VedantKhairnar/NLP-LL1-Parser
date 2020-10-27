import ll_gramtools
import ll_parser
import re

def ll_table(ll_g):
    '''
    returns the ll_parsing table, given the ll_grammar as param
    '''
    table = {}
    prods = ll_g.first
    #filling in the table with first sets
    for n_term in prods:
        table[n_term] = {}
        #row entery of the non terminal
        for rule in prods[n_term]:
            for term in prods[n_term][rule]:
                #if the corresponding column is filled, raise error 
                if term in table[n_term]:
                    print ("Not LL(1) Grammar")
                    #raise Exception
                if rule != '':
                    table[n_term][term] = rule

    #using the follow set
    foll = ll_g.follow
    for n_term in foll:
        if '' in prods[n_term]:
            for term in foll[n_term]:
                if not table[n_term].get(term, None):
                    table[n_term][term] = ''

    return table

def get_parser(rules):
    '''rules is the string that contains all grammar rules'''
    g = ll_gramtools.get_ll_grammar(rules)
    par = ll_parser.parser(g)
    par.set_table(ll_table(g))
    return par


def get_input(scanner, text):
	'''
	puts input in acceptable form for the parser
	'''
	tokens, remainder = scanner.scan(text)
	return tokens


if __name__ == '__main__':
    g = \
    '''E : T X
    X : + E X | 
    T : F Y
    Y : * T Y | 
    F : int | ( E )'''

    g = """S : NP_Sg VP_Sg | NP_Pl VP_Pl
NP : NP_Pl | NP_Sg
NP_Sg : N_Sg | Det_Sg N_Sg | Det_Both N_Sg | Adj N_Sg | Det_Sg Adj N_Sg | Det_Both Adj N_Sg| PropN_Sg
NP_Pl : N_Pl | Det_Pl N_Pl | Det_Both N_Pl | Adj N_Pl | Det_Pl Adj N_Pl | Det_Both Adj N_Pl| PropN_Pl
VP_Sg : IV_Pres_Sg | IV_Past | TV_Pres_Sg | TV_Past | TV_Pres_Sg NP | TV_Past NP | Adv IV_Pres_Sg | Adv IV_Past | Adv TV_Pres_Sg NP | Adv TV_Past NP
VP_Pl : IV_Pres_Pl | IV_Past | TV_Pres_Pl | TV_Past | TV_Pres_Pl NP | TV_Past NP | Adv IV_Pres_Pl | Adv IV_Past | Adv TV_Pres_Pl NP | Adv TV_Past NP
N_Pl : girls | boys | children | cars | apples | dogs
Adj : good | bad | beautiful | innocent
Adv : happily | sadly | nicely
N_Sg : dog | girl | car | child | apple | elephant
PropN_Sg : rashmi | piyumika
PropN_Pl : they | i
Det_Sg : this | every | a | an
Det_Pl : these | all
Det_Both : some | the | several
IV_Pres_Sg : dissappeares | walks
TV_Pres_Sg : sees | likes |eat
IV_Pres_Pl : dissappear | walk
TV_Pres_Pl : see | like
IV_Past : dissappeared | walked
TV_Past : saw | liked | ate | shot"""


    p = get_parser(g)
    input = 'rashmi likes apple'
    input = input.split(" ")
    print ('\n'+ str(p.table)+ '\n')
    v = p.parse(input)
    print (v)

    input = 'rashmi like apple'
    input = input.split(" ")
    print ('\n'+ str(p.table)+ '\n')
    op = p.parse(input)
    print(op)