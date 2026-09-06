class Solution:

    def encode(self, strs: List[str]) -> str:
        # get the length of each word in the list
        encoded_str = []

        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append("#")
            encoded_str.append(s)

        return "".join(encoded_str) # the encoded string
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            delimiter = s.find("#", i)
            length = int(s[i:delimiter])
            start_id = delimiter + 1
            end_id = start_id + length
            decoded_str.append(s[start_id : end_id])
            i = end_id

        return decoded_str
