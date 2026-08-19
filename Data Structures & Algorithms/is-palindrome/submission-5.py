class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = s.replace(" ",'').replace("?","").replace("  ","").replace("'","").replace(",","").lower()
        # s3 = ""
        # for i in s2:
        #     s3 = i + s3
        # if s2 != s3:
        #     return False
        # else:
        #     return True

        r = "".join([x for x in s if x.isalnum()])

        return r.lower() == r[::-1].lower()