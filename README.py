class values:
    wordCount = 0
    sentenceCount = 0
    charCount = 0

    def __init__(self, text):
        #increment for first word
        self.wordCount += 1

        for i in range(len(text)):
            if text[i].isalpha():
                self.charCount += 1
            elif text[i] == ' ' and text[i+1] != ' ':
                self.wordCount += 1
            elif (text[i] == '?') or (text[i] == '.') or (text[i] == '!'):
                self.sentenceCount += 1
            else: # if equals other symbols %$#@*
                if self.wordCount > self.charCount: # if only symbols are entered (words cannot be more than char)
                    self.wordCount = 0

    def calcIndex(self):
        if self.wordCount != 0: # calculate only when word != 0, otherwise division by 0 error
            L = (self.charCount*100)/self.wordCount
            S = (self.sentenceCount*100)/self.wordCount
            index = round(((0.0588 * L) - (0.296 * S) - 15.8))
            return index
        else:
            return 0


text = input("Enter text: ")
Valv = values(text)
print(f"Word count: {Valv.wordCount}, sentence count: {Valv.sentenceCount}, charCount: {Valv.charCount}")
index = Valv.calcIndex()
if (index < 1):
    print("Before Grade 1\n")
elif (index > 16):
    print("Grade 16+")
else:
    print(f"Grade{index}")



