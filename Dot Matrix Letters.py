'''
11/2019 Ruizhi Ou (Melody Joy)
'''

# Initialize variables for dot matrix letters

A = ['  *  ',
     ' * * ',
     '*****',
     '*   *',
     '*   *']


B = ['**** ',
     ' *  *',
     ' *** ',
     ' *  *',
     '**** ']


C = [' *** ',
     '*    ',
     '*    ',
     '*    ',
     ' *** ']


D = ['**** ',
     ' *  *',
     ' *  *',
     ' *  *',
     '**** ']


E = ['*****',
     '*    ',
     '***  ',
     '*    ',
     '*****']


F = ['*****',
     '*    ',
     '**** ',
     '*    ',
     '*    ']


G = [' ****',
     '*    ',
     '*  **',
     '*   *',
     ' ****']


H = ['*   *',
     '*   *',
     '*****',
     '*   *',
     '*   *']


I = [' *** ',
     '  *  ',
     '  *  ',
     '  *  ',
     ' *** ']


J = ['*****',
     '   * ',
     '   * ',
     '*  * ',
     ' **  ']


K = ['*   *',
     '*  * ',
     '***  ',
     '*  * ',
     '*   *']


L = ['*    ',
     '*    ',
     '*    ',
     '*    ',
     '*****']


M = ['*   *',
     '** **',
     '* * *',
     '*   *',
     '*   *']


N = ['*   *',
     '**  *',
     '* * *',
     '*  **',
     '*   *']


O = [' *** ',
     '*   *',
     '*   *',
     '*   *',
     ' *** ']


P = ['**** ',
     '*   *',
     '**** ',
     '*    ',
     '*    ']


Q = [' *** ',
     '*   *',
     '* * *',
     '*  * ',
     ' ** *']


R = ['**** ',
     '*   *',
     '**** ',
     '*   *',
     '*   *']


S = [' *** ',
     '*    ',
     ' *** ',
     '    *',
     '**** ']


T = ['*****',
     '  *  ',
     '  *  ',
     '  *  ',
     '  *  ']


U = ['*   *',
     '*   *',
     '*   *',
     '*   *',
     ' *** ']


V = ['*   *',
     '*   *',
     '*   *',
     ' * * ',
     '  *  ']


W = ['*   *',
     '* * *',
     '* * *',
     ' * * ',
     ' * * ']


X = ['*   *',
     ' * * ',
     '  *  ',
     ' * * ',
     '*   *'] 


Y = ['*   *',
     ' * * ',
     '  *  ',
     '  *  ',
     '  *  ']


Z = ['*****',
     '   * ',
     '  *  ',
     ' *   ',
     '*****'] 

space_between_letters = [' ',
                         ' ',
                         ' ',
                         ' ',
                         ' ']


space_between_words = ['   ',
                       '   ',
                       '   ',
                       '   ',
                       '   ']



dot_matrix_letters = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 
                      'F': F, 'G': G, 'H': H, 'I': I, 'J': J,
                      'K': K, 'L': L, 'M': M, 'N': N, 'O': O,
                      'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
                      'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y,
                      'Z': Z, ' ': space_between_words}


# Initialize an empty list to store the result

result = ['',
          '',
          '',
          '',
          '']


# Get the input phrase

print("Please enter the letters you want to convert to dot matrix letters.")

s = input()



# Delete all non-letter characters

for char in s:

    if char.isalpha() == False and char.isspace() == False:

        idx = s.index(char)

        s = s[0:idx] + s[idx+1:len(s)]



# List that separates and saves each letter

s = s.upper()

phrase = list(s)



# Walk through one line after another

for row in range(5):

    # Walk through every letter in the given string

    for index in range(len(phrase)):

        letter = dot_matrix_letters[phrase[index]]
    
        result[row] += letter[row]

        result[row] += space_between_letters[row]


for letter in result:

    print(letter)


