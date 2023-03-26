class Solution:
    def get_base(self, s, m, e, w):
        min_l = []
        for i in range(w):
            min_n = 101
            for j in range(e):
                if m[j][i] < min_n:
                    min_n = m[j][i]
            min_l.append(min_n)
        for i in range(w):
            for j in range(min_l[i]):
                s.append(i)
            for j in range(e):
                m[j][i] -= min_l[i]
    
    def read_input(self):
        t = int(input())
        s = []
        for i in range(t):
            line = input().split()
            e = int(line[0])
            w = int(line[1])
            m = []
            for j in range(e):
                m.append([])
                line = input().split()
                for k in range(w):
                    m[j].append(int(line[k]))
            
            s.clear()
            self.get_base(s, m, e, w)
            print('s: ')
            for j in s:
                print(j, end=' ')
            print()
            print('m: ')
            for j in range(e):
                for k in range(w):
                    print(m[j][k], end=' ')
                print()


sol = Solution()
sol.read_input()
            
