# file: ribosome.py
# authors: Jason Morse & Wantong Liu
# date: May 3, 2013
#

import string

def makeDelta():
    def insert((key, value), dictionary):
        dictionary[key] = value
        return dictionary
    
    def fold(f, list, id):
        if list == []:
            return id
        else:
            return f(list[0], fold(f, list[1:], id))

    def sep(a, b, c, d):
        return [((a, b), (c, d))]

    others1 = sep(0,'U', '' ,1) + sep(0,'C', '',6) + sep(0,'A','', 11) + sep(0,'G','', 16) + sep(1,'U', '' ,2) + sep(1,'C', '' ,3) + sep(1,'A', '',4) + sep(1,'G', '',5) + sep(2,'U','Phe ',0) + sep(2,'C','Phe ',0) + sep(2,'A','Leu ',0) + sep(2,'G','Leu ',0)
    others2 = sep(6,'C','', 8) + sep(8,'U','Pro ', 0)+ sep(8,'C','Pro ', 0)+ sep(8,'A','Pro ', 0)+ sep(8,'G','Pro ', 0)
    others3 = sep(1,'A','', 4) + sep(4,'U','Tyr ',0)+ sep(4, 'C', 'Tyr ', 0)+ sep(4, 'A', 'Stop', 0)+ sep(4, 'G', 'Stop', 0)
    others4 = sep(1,'G','', 5) + sep(5,'U','Cys ', 0) + sep(5,'C','Cys ', 0) + sep(5,'A','Stop', 0) + sep(5,'G','Trp ', 0)
    others5 = sep(6,'A','', 9) + sep(9,'U','His ', 0)+ sep(9,'C','His ', 0)+ sep(9,'A','Gln ', 0)+ sep(9,'G','Gln ', 0)
    others6 = sep(1,'C','',3) + sep(3,'U','Ser ',0) + sep(3, 'C', 'Ser ', 0) + sep(3, 'A', 'Ser ', 0) + sep(3, 'G', 'Ser ', 0)
    others7 = sep(6,'U','', 7) + sep(7,'U','Leu ', 0)+ sep(7,'C','Leu ', 0)+ sep(7,'A','Leu ', 0)+ sep(7,'G','Leu ', 0)
    others8 = sep(6,'G','', 10) + sep(10,'U','Arg ', 0)+ sep(10,'C','Arg ', 0)+ sep(10,'A','Arg ', 0)+ sep(10,'G','Arg ', 0)
    others9 = sep(11,'U','',12) + sep(12, 'U', 'Lle ', 0) + sep(12, 'C', 'Lle ', 0) + sep(12, 'A', 'Lle ', 0) + sep(12, 'G', 'Met ', 0)
    others10 = sep(11,'C', '', 13) + sep(13, 'U', 'Thr ',0) + sep(13, 'C', 'Thr ',0)+ sep(13, 'A', 'Thr ',0) + sep(13, 'G', 'Thr ',0)
    others11 = sep(11,'A', '', 14) + sep(14, 'U', 'Asn ',0) + sep(14, 'C', 'Asn ',0)+ sep(14, 'A', 'Lys ',0) + sep(14, 'G', 'Lys ',0)
    others12 = sep(11,'G', '', 15) + sep(15, 'U', 'Ser ',0) + sep(15, 'C', 'Ser ',0)+ sep(15, 'A', 'Arg ',0) + sep(15, 'G', 'Arg ',0)
    others13 = sep(16,'C', '', 18) + sep(18, 'U', 'Ala ',0) + sep(18, 'C', 'Ala ',0)+ sep(18, 'A', 'Ala ',0) + sep(18, 'G', 'Ala ',0)
    others14 = sep(16,'U', '', 17) + sep(17, 'U', 'Val ',0) + sep(17, 'C', 'Val ',0)+ sep(17, 'A', 'Val ',0) + sep(17, 'G', 'Val ',0)
    others15 = sep(16,'G', '', 20) + sep(20, 'U', 'Gly ',0) + sep(20, 'C', 'Gly ',0)+ sep(20, 'A', 'Gly ',0) + sep(20, 'G', 'Gly ',0)
    others16 = sep(16,'A', '', 19) + sep(19, 'U', 'Asp ',0) + sep(19, 'C', 'Asp ',0)+ sep(19, 'A', 'Glu ',0) + sep(19, 'G', 'Glu ',0)
    
    transitions =  others1 + others2 + others3 + others4 + others5 + others6 + others7 + others8 + others9 + others10 + others11 + others12 + others13 + others14 + others15 + others16
    delta = fold(insert, transitions, {})
    
    return delta

def runFSM(M, state, input, answer):
    
    (A, Q, delta, _, F) = M
    
    while len(input)!= 0:
        
        symbol = input[0]
        key = (state, symbol)
        
        if  (delta[key][0] == 'Stop'):
            return answer
        else:
            state = delta[key][1]
            answer += delta[key][0]
            input = input[1:]
            
    return answer

ribosomeMachine = (['A', 'U', 'C', 'G'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], makeDelta(), 0, [0])

def ribosome(mRNA):
    return runFSM(ribosomeMachine, 0, mRNA, '')
