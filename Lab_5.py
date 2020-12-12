


"""
The program is trying to tanslate a sentence as user input.
We first read in the text file textese.txt.
then from the text file, we create a list of stings from each lines in the text file.
Then, we create a dictionary the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an
array of stings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we 
loop through each words, find the key matching the word and returns back the value tied to the word
into our dictionary.

After each word is translated, we then
print out the translated sentence to the user.
"""

"""
main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    words = for each of the word in the sentence,
    for each words, translate the word
    print translated sentence to user

 create_dictionary():
    read in textese.txt
    create list = each line from file
    close the file
    create a dict off of the list
    return the dict
        
main()
"""

def main():
    sentence = "enjoy the excellent band tonight"
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()

    print("words", words)
    translation = {}
    for word in words: # "tonight,2nite"
        [k, v] = word.split(",") #["tonight,2nite"]
        translation[k] = v
    #print(translation)
    return translation

def translate(sentence, dictionary):
    print("From translate", sentence)
    words = sentence.split() #["enjoy", "the", "excellent", "band", "tonight",]
    for word in words:
        print(dictionary.get(word, word), " ", end="")

main()



