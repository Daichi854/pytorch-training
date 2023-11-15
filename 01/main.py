from utils.function import add
from utils.count import count_word

if __name__ == "__main__":
    n = add(1,2)
    s = "hello world"
    print(n)
    print("e" , count_word(s, 'e'))
    print("o" , count_word(s, 'o'))    
    print("l" , count_word(s, 'l'))

