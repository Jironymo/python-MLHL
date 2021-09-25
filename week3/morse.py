class morse:
    def __init__(self, format = False):

        self.result = []

        self.eom_flag = True
        self.eol_flag = True
        self.symbolic_format = False
        
        self.dict = {
            'dot': 'di',
            'dash': 'dah',
            'space':', ',
            'eol': 'dit',   # end of letter
            'eom': '.'      # end of message 
            }

        if format:
            self.symbolic_format = self.is_symbolic(format)
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
            self.result.append(self.dict['eom'])
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

    def is_symbolic(self, format: str) -> bool:
        self.symbolic_format = (format.find(' ') == -1)
        return self.symbolic_format
    
    def parse_format(self, format: str) -> list:
        if self.symbolic_format:
            return list(format)
        return format.split(' ')

    def update_dict(self, format: str) -> bool:
        format_list = self.parse_format(format)
        format_len = len(format_list)
        assert 2 <= format_len <= 4, "format should have between  2 and 4 params (both ends including)" 

        # before updating dict based on number of input params,
        # update it based on whether it is symbolic
        # Признаюсь, данный эджкейс кажется костыльно представленным в задании. = (
        # Пришлось догадываться из примеров инпута-аутпута
        if self.symbolic_format:
            self.dict['space'] = ' '
            self.dict['eol'] = '.'
            self.dict['eom'] = ''

        if format_len == 2:
            self.dict['dot'] = format_list[0]
            self.dict['dash'] = format_list[1]
        
        if format_len == 3:
            self.dict['dot'] = format_list[0]
            self.dict['eol'] = format_list[1]
            self.dict['dash'] = format_list[2]
        
        if format_len == 4:
            self.dict['dot'] = format_list[0]
            self.dict['eol'] = format_list[1]
            self.dict['dash'] = format_list[2]
            self.dict['eom'] = format_list[3]

        return

    def __str__(self):
        # TODO make it print out correctly
        return str(self.result[::-1])

if __name__ == "__main__":

    print(-+morse())
    print(-++~+-+morse())
    print(--+~-~-++~+++-morse())
    print(--+~-~-++~+++-morse(".-"))
    print(--+~-~-++~+++-morse("..-"))
    print(--+~-~-++~+++-morse("._-|"))
    print(--+~-~-++~+++-morse("dot DOT dash"))
    print(--+~-~-++~+++-morse("ai aui oi "))
    print(--+~-~-++~+++-morse("dot dot dash ///"))