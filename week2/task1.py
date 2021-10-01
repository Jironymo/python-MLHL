import re

def notBadReplacer(string):
    '''replace all occurences of "not ... bad" in *string* using RegExp'''
    # use non-greedy quanifier to match the first occurence of the pattern
    return re.sub('(not)(.+?)(bad)', 'good', string)

def decimalSummator(string):
    # enlist all occurences of consecutive number
    # use !generator comprehension instead of list in case the string is long
    list_of_nums = [int(num) for num in re.findall('\d+', string)]
    return sum(list_of_nums)

def isScrollingPermutation(str1, str2):
    return str2 in str1+str1

def sentenceReverser(string):
    pattern = '([A-Za-z0-9]+|[.?!])'
    list_of_words = re.findall(pattern, string)
    print(f'list of words: {list_of_words}')
    # check if the last character was an ending mark
    if list_of_words[-1].isalnum():
        return ' '.join(list_of_words[::-1])
    else:
        # add the last mark explicitly if it was present in the input sentence
        return ' '.join(list_of_words[len(list_of_words)-2::-1]) + list_of_words[-1]

# if __name__=='__main__':
    # check_not_bad = {
    # 'ex1': 'This dinner is not that bad!', 
    # 'ex2': 'not not bad bad', 
    # 'ex3': 'not das not bad not bad not das sda bad not',
    # 'ex4': 'nothingbad ha'
    # }

    # check_decimal_sum = {
    # 'ex1': '13213 das 31o38219 dksaj 38913819', 
    # 'ex2': '31231dsakdjak', 
    # 'ex3': '392m321djkasjdak832'
    # }
    
    # print('\nsubtask 1.1:')
    # for key, value in check_not_bad.items():
        # print(notBadReplacer(value))
    
    # print('\nsubtask 1.2:')
    # for key, value in check_decimal_sum.items():
        # print(decimalSummator(value))
    
    # print('\nsubtask1.3:')
    # for key, value in check_not_bad.items():
        # print(sentenceReverser(value))

    # print(isScrollingPermutation('abs', 'bab'))