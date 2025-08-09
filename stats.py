
def get_book_text(filepath):
    filepathstring = filepath.read()
    return filepathstring

def main(booklink):
    with open(booklink) as file:
        output = get_book_text(file)
        print(output)

def wordcount(booklink):
     with open(booklink) as file:
         bookstring = get_book_text(file)
         words = bookstring.split()
         no_of_words = len(words)
         return no_of_words

def charactercount(booklink):
    charactercountdict = {}
    with open(booklink) as file:
        bookstring = get_book_text(file)
        for character in bookstring:
            character = character.lower()
            if character not in charactercountdict:
                charactercountdict[character] = 1
            else:
                charactercountdict[character] += 1
        return charactercountdict

def sort_on(items):
    return items["num"]

def sort_dict(booklink):
    charactercountdict = charactercount(booklink)
    sorted_dict = {}
    temp_sort_list = []
    for char, num in charactercountdict.items():
        if char.isalpha() == True:
            sorted_dict = {"char": char, "num": num}
            temp_sort_list.append(sorted_dict)
    temp_sort_list.sort(reverse=True, key=sort_on)
    return temp_sort_list

