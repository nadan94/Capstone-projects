#DNA_num = input("Please enter the DNA sequence :").upper()

def translate(DNA_seq):
    amino = ""
    #iterates every 3rd char
    for i in range(0, len(DNA_seq), 3):
        #Loops through 3 chars at a time(makes 3 chars one iteration)
         if (DNA_seq[i:i+3] == 'ATT') or (DNA_seq[i:i+3] == 'ATC') or (DNA_seq[i:i+3] == 'ATA'):
             amino+=('I')#If the condition is met append it to the string 'amino'
         elif (DNA_seq[i:i+3] == 'CTT') or (DNA_seq[i:i+3] == 'CTC') or (DNA_seq[i:i+3] == 'CTA')or (DNA_seq[i:i+3] == 'CTG') or (DNA_seq[i:i+3] == 'TTA') or (DNA_seq[i:i+3] == 'TTG'):
             amino+=('L')
         elif (DNA_seq[i:i+3] == 'GTT') or (DNA_seq[i:i+3] == 'GTC') or (DNA_seq[i:i+3] == 'GTA') or (DNA_seq[i:i+3] == 'GTG'):
             amino+=('V')
         elif (DNA_seq[i:i+3] == 'TTT') or (DNA_seq[i:i+3] == 'TTC'):
             amino+=('F')
         elif (DNA_seq[i:i+3] == 'ATG'):
             amino+=('M')
         else:
             #Any other sequence will return 'X'
             amino+=('X')
    return amino 


def mutate():
    #Opens the textfile 'DNA.txt'
    with open('DNA.txt', 'r+') as mut_DNA_read:
        DNA_read = mut_DNA_read.read()
        replaceString = ""
        for l in range(0, len(DNA_read)):
            #searches for the lower case in the read textfile
            if DNA_read[l].islower():
                #appends the empty string with the found lower case
                replaceString = replaceString + (DNA_read[l])
        return replaceString
                

with open('DNA.txt', 'r+') as mut_DNA_read2:
        DNA_read2 = mut_DNA_read2.read()

#Replacing the lowercase 'a'
mutate_replace_normal = DNA_read2.replace(mutate(), 'A')
mutate_replace_mutated = DNA_read2.replace(mutate(), 'T')

with open('normalDNA.txt', 'w') as normalDNA_write:
    normalDNA_write.write(mutate_replace_normal)

with open('mutatedDNA.txt', 'w') as mutatedDNA_write:
    mutatedDNA_write.write(mutate_replace_mutated)

with open('normalDNA.txt', 'r+') as normalDNA_read:
    normal_txt = normalDNA_read.read()

with open('mutatedDNA.txt', 'r+') as mutatedDNA_read:
    mutated_txt = mutatedDNA_read.read()
    
def txtTranslate(DNA_seq):
    translate_normut = translate(DNA_seq)
    return translate_normut

   
print("The DNA sequence for the normal text is: \n{0}".format(txtTranslate(normal_txt)))
print("\nThe DNA sequence for the mutated text is: \n{0}".format(txtTranslate(mutated_txt)))



  
