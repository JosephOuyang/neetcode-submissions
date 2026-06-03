class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for i in range(len(strs)):
            encodedString += str(len(strs[i])) + '_' + strs[i]
        return encodedString

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            delimIndex = s.find('_', i)
            strLength = int(s[i : delimIndex])
            decoded.append(s[delimIndex + 1 : delimIndex + 1 + strLength])
            i = delimIndex + 1 + strLength
        return decoded

