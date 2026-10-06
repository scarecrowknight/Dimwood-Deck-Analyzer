class Parser:

        def splitAtN(self, string, n):
                return string[:n], string[n:]
        def splitAtNAsInt(self, string, n):
                return int(string[:n], 16), string[n:]


        # throughout the savefile there are a number of sections that tell you the length of the next information group with 2 digits of hex
        # this is used all throughout the parsers to unpack those parts of the string 
        def getNext(self, string):
                dataLength, string = self.splitAtNAsInt(string, 2)
                data, string = self.splitAtN(string, dataLength)
                return data, string

                