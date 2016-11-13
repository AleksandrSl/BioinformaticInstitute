class FastqRead():
    """
       Represent one read in fastq format
    """
    min_aver_qual = 30 # Что-то типо статической переменной, насколько я прочитал
    # sequence = [] Я так полагаю от этого смысла нет
    # quality = []
    # name = ''

    def __init__(self, fastq_handle):
        try:
            temp = []
            for _ in range(4):
                temp.append(next(fastq_handle).strip())
            if not temp[0].startswith('@') or temp[1][0] not in 'ACTG':
                raise ValueError('This is not a fastq file')
            assert len(temp[1]) == len(temp[3])
            self.name, self.sequence, _, self.quality = temp
            self.length = len(self.sequence)
            # self.min_aver_qual = min_aver_qual
            # self.i = 0
        except StopIteration:
            print('The end of file reached!')

    def aver_qual(self, zero_char = '!'):
        translated_quality_seq = [ord(el) - ord(zero_char) for el in self.quality]
        return round(sum(translated_quality_seq) / self.length, 3)

    def seq_at(self, i):
        if i >= 0 and i < self.length:
            return self.sequence[i]
        else:
            raise IndexError()

    def qual_at(self, i):
        if i >= 0 and i < self.length:
            return self.quality[i]
        else:
            raise IndexError()

    def good(self):
        return self.aver_qual() > self.min_aver_qual

    def __len__(self):
        return self.length

    def __str__(self):
        return "{}\n{}\n+\n{}".format(self.name, self.sequence, self.quality)

    # def __repr__(self):
    #     pass

    def __getitem__(self, i):
        """
        :param i: position
        :return: tuple of sequence and quality at i position
        """
        return self.seq_at(i), self.qual_at(i)

    def __iter__(self): # Generator
        counter = 0
        while counter < self.length:
            yield self[counter]
            counter += 1

    # def __iter__(self): # Iterator
    #     return self

    # def __next__(self):
    #     if self.i < len(self.sequence):
    #         i = self.i
    #         self.i += 1
    #         return self[i]
    #     else:
    #         raise StopIteration()