class Solution:
    numbers = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits == ""):
            return []
        num_3 = 0
        num_4 = 0
        num_letters = []
        for i in digits:
            if i in '79':
                num_4 += 1
                num_letters.append(4)
            else:
                num_3 += 1
                num_letters.append(3)
        num_combinations = (3**num_3) * (4**num_4)
        combinations = [""]* ((3**num_3) * (4**num_4))
        number_iterations = 1
        for digit in digits:
            num_combinations //= len(self.numbers[digit])
            counter = 0
            for i in range(number_iterations):
                for letter in self.numbers[digit]:
                    for j in range(num_combinations):
                        combinations[counter] += letter
                        counter += 1        
            
            number_iterations *= len(self.numbers[digit])
        return combinations

a = Solution()
a.letterCombinations("7")