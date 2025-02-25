def modify_string(txt):
    vowels = "aeiouAEIOU"
    result = []
    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1)%3 == 0 and i + 1 != len(txt):
            if char in vowels or (i>0 and result[-2] == '_'):
                result.append(txt[i+1])
            result.append('_')
    return  ''.join(result)

if __name__ == '__main__':
    print(f"Input 1: hello\nOutput 1: {modify_string("hello")}"
          f"\nInput 2: assalom\nOutput 2: {modify_string("assalom")}"
          f"\nInput 3: abcabcdabcdeabcdefabcdefg\nOutput 3: {modify_string("abcabcdabcdeabcdefabcdefg")}")