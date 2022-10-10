# Mayolo Valencia
# 11/14/2021
# User inputs a sequence or sequences of nucleotides then the
# method filters through the input, taking away any numbers and spaces
# then sends and error if it theres not a right amount of characters for
# a set. It then figures out if the set is in the dictionary or not.

# length of the set
SET_LENGTH = 3

# starts global variable with a dictionary
DNA_SEQUENCES = {'TTT': 'Phe', 'TCT': 'Ser', 'TGT': 'Cys', 'TAT': 'Tyr',
                 'TTC': 'Phe', 'TCC': 'Ser', 'TGC': 'Cys', 'TAC': 'Tyr',
                 'TTG': 'Leu', 'TCG': 'Ser', 'TGG': 'Trp', 'TAG': '***',
                 'TTA': 'Leu', 'TCA': 'Ser', 'TGA': '***', 'TAA': '***',
                 'CTT': 'Leu', 'CCT': 'Pro', 'CGT': 'Arg', 'CAT': 'His',
                 'CTC': 'Leu', 'CCC': 'Pro', 'CGC': 'Arg', 'CAC': 'His',
                 'CTG': 'Leu', 'CCG': 'Pro', 'CGG': 'Arg', 'CAG': 'Gln',
                 'CTA': 'Leu', 'CCA': 'Pro', 'CGA': 'Arg', 'CAA': 'Gln',
                 'GTT': 'Val', 'GCT': 'Ala', 'GGT': 'Gly', 'GAT': 'Asp',
                 'GTC': 'Val', 'GCC': 'Ala', 'GGC': 'Gly', 'GAC': 'Asp',
                 'GTG': 'Val', 'GCG': 'Ala', 'GGG': 'Gly', 'GAG': 'Glu',
                 'GTA': 'Val', 'GCA': 'Ala', 'GGA': 'Gly', 'GAA': 'Glu',
                 'ATT': 'Ile', 'ACT': 'Thr', 'AGT': 'Ser', 'AAT': 'Asn',
                 'ATC': 'Ile', 'ACC': 'Thr', 'AGC': 'Ser', 'AAC': 'Asn',
                 'ATG': 'Met', 'ACG': 'Thr', 'AGG': 'Arg', 'AAG': 'Lys',
                 'ATA': 'Ile', 'ACA': 'Thr', 'AGA': 'Arg', 'AAA': 'Lys'}

def clean_sequence(string_input):
    """ Cleans the string from numbers,spaces
        and capitolizes every character
    """
    
    # open string
    clean_str = ""
    
    # if the character is a letter put into the open string
    for char in string_input:
        if char.isalpha():
            clean_str += char.upper()
            
    return clean_str

def is_complete_triple(user_input):            
    """ If the string is not a divisible by 3
        return false else true
    """
    
    complete_triple = len(user_input) % SET_LENGTH == 0   
    return complete_triple
        
def main():
    """ if user presses enter program stops else it
        continues to run and goes through the following
        steps. Cleans string, check if its divisible by 3,
        serperates into 3's, prints keys and values
    """
    
    # intilizing the variable
    prompt_user = True
    
    # continues asking the user for more nucleotides
    while prompt_user :
        
        # user inputs sequence
        sequence = input("Enter a nucleotide sequence," \
                 " or just press ENTER to quit: ")
        
        # if they press enter the ending variable becomes true
        # and breaks out of the while loop
        if sequence == "":
            prompt_user = False
            
        # runs the method to get results
        else:
            clean_str = clean_sequence(sequence)
            
            if not is_complete_triple(clean_str):
                print("Error: You must give complete triples. \n")
            
            # returns the values for the keys
            else:
                
                # seperates the clean string into a list of sets 
                triple_sets = [clean_str[index: index + SET_LENGTH] \
                               for index in range(0, len(clean_str), SET_LENGTH)]

                # find if the set is in the dictonary or not then prints accordingly
                for set in triple_sets:
                    amino_acid = DNA_SEQUENCES.get(set, "invalid sequence")
                    print(set, amino_acid)
                        
# runs main method for everything to work
main()
    
    