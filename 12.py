class word_frequency():
    def __init__(self, my_file=''):
        file = open('letter.txt', 'r')
        content = file.read()  # Tüm içeriği al
        sentences = content.split('.')  # '.'lara ayır
        self.words = []

        for sentence in sentences:
            words_in_the_sentence = sentence.split(' ')
            for word in words_in_the_sentence:  # karakter istenirse bir for döngüsü daha kullanılmalı
                self.words.append(word)

        # print(self.words)

    def frequency_1(self):
        self.frequency_list1 = {}
        for i in self.words:
            if i in self.frequency_list1:
                self.frequency_list1[i] += 1
            else:
                self.frequency_list1[i] = 1

    def frequency_2(self):
        self.frequency_list2 = {}
        for i in range(len(self.words) - 1):
            word_1, word_2 = self.words[i], self.words[i + 1]
            if (word_1, word_2) in self.frequency_list2:
                self.frequency_list2[word_1, word_2] += 1
            else:
                self.frequency_list2[word_1, word_2] = 1

    def write_frequency_1(self):
        for w_1 in self.frequency_list1:
            print(w_1 + ' ' + str(self.frequency_list1[w_1]))

    def write_frequency_2(self):
        for w_2 in self.frequency_list2:
            print(str(w_2) + ' ' + str(self.frequency_list2[w_2]))


my_class_1 = word_frequency()
my_class_1.frequency_2()
my_class_1.write_frequency_2()