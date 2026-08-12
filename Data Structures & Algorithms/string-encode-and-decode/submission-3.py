class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for element in strs:
            for character in element:
                encoded += str(ord(character))
                encoded += '*'
            encoded += '#'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        letter = ''
        word = ''
        for character in s:
            if character != '*' and character != '#':
                letter += character
            if character == '*':
                word += chr(int(letter))
                letter = ''
            if character == '#':
                decoded_list.append(word)
                word = ''
        return decoded_list