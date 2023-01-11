
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l = 0
        r = min(1, len(fruits)-1)
        max_size = r-l+1

        self.freq = {}
        self.add_freq(fruits[l])
        self.add_freq(fruits[r])

        while True:
            
            unique_len = self.calc_unique()

            if unique_len <= 2: 
                max_size = max(max_size, r-l+1)
                r+=1
                if r >= len(fruits):
                    break
                self.add_freq(fruits[r])
            else:
                self.rm_freq(fruits[l])
                l+= 1

        return max_size

    def add_freq(self, val):
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

    def rm_freq(self, val):
        self.freq[val] -= 1

    def calc_unique(self):
        unique = 0
        to_remove = []
        for k, v in self.freq.items():
            if v > 0:
                unique+=1
            if v == 0:
                to_remove.append(k)

        for i in to_remove:
            del self.freq[i]

        return unique
