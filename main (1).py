from string import punctuation


# 1. Create the documents dictionary
# ----------------------------------

def get_documents(filename):

    # read the input file
    with open(filename, "r") as fp:
        lines = fp.readlines()

    # remove the first line and join all reminding line into one text
    lines.pop(0)
    text = "".join(lines)

    # split the text into a list of documents
    docs = text.split("\n<NEW DOCUMENT>\n")

    # convert the list into a dictionary
    documents = {i+1: doc for i, doc in enumerate(docs)}

    return documents


# 2. Create the word index dictionary
# -----------------------------------

def get_index(documents):

    index = {}

    for i, doc in documents.items():

        # clean the document
        doc = doc.lower()
        words = doc.split()

        for word in words:

            # remove punctuation
            word = word.strip()
            w = [char for char in word if char not in punctuation]
            word = "".join(w)

            # add the word to the dictionary
            if word in index:
                index[word].add(i)
            else:
                index[word] = {i}

    return index


# 3. Find the intersection of documents that contains a set of words
# ------------------------------------------------------------------

def find_documents(index, words):

    # get the last word
    word = words.pop()

    if word in index:
        docs = index.get(word, set())

    # do the intersection with the others
    for word in words:
        cited_in = index.get(word, set())
        docs = docs.intersection(cited_in)

    return docs


# 4. Main Loop
# ------------

def main(filename):

    # compute the document and the index
    documents = get_documents(filename)
    index = get_index(documents)

    OPTIONS = ["1. Search for documents",
               "2. Read Document",
               "3. Quit Program"]

    while True:

        # print the menu
        print("\nWhat would you like to do?")
        for option in OPTIONS:
            print(option)

        choice = input("> ")

        if choice == "1":
            words = input("Enter search words: ")

            # treat the words
            words = words.lower().split()
            words = [word.strip() for word in words]

            # get the cited documents
            docs = find_documents(index, words)

            # convert numbers to strings
            docs_string = [str(doc) for doc in docs]
            result = " ".join(docs_string)

            print("\nDocuments fitting search:")
            print(result)

        elif choice == "2":

            doc = int(input("Enter document number: "))

            # in case the number is incorrect
            if doc not in documents:
                print("Invalid document number")

            # in case the number is valid
            else:
                print(f"Document #{doc}")
                print("------------------")

                print(documents[doc])
                print("------------------")

        # exit the loop
        elif choice == "3":
            break

        # invalid choice
        else:
            pass


if __name__ == "__main__":

    filename = "ap_docs.txt"
    main(filename)
