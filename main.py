# алгоритм подсчета символов в строке
# считать сколько и каких букв есть в нашей строке
# пример: "привет" - (п - 1, р - 1, и - 1, в - 1, е - 1, т - 1)

# алгоритм
def strcounter(s: str):
    symbols_dict = {} # {symb: counter}
    for symbol in s:
        if symbol in symbols_dict:
            symbols_dict[symbol] += 1
        else:
            symbols_dict[symbol] = 1
    print(symbols_dict)
        
    # O(N)
strcounter("оооооооббббббббббббааааааааааа")