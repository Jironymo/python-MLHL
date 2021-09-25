class morse:
    def __init__(self, format = False):

        self.eom_flag = True
        self.eol_flag = True
        self.result = []
        self.dict = {
            'dash': 'dah',
            'dot': 'di',
            'space':', ',
            'eol': 'dit',   # end of letter
            'eom': '.'      # end of message 
            }

        if format: 
            self.update_dict(format)

    def __pos__(self):
        """
        implements dot
        """

        if self.eom_flag:
            self.result.append('.')
            self.eom_flag = False

        if self.eol_flag:
            self.result.append(self.dict['eol'])
            self.eol_flag = False
        else:
            self.result.append(self.dict['dot'])

        return self

    def __neg__(self):
        """
        implements dash
        """

        if self.eom_flag:
            self.result.append('.')
            self.eom_flag = False
            
        self.result.append(self.dict['dash'])
        return self

    def __invert__(self):
        """
        implements space
        """

        # enable eol flag after space is encountered
        # since next dot is to be eol
        self.eol_flag = True
        self.result.append(self.dict['space'])
        return self

    def update_dict(self):
        pass

    def __str__(self):
        # return str(self.result[::-1])
        # return ''


a = -++~+-+morse()
print(a)