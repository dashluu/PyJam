class Solution:
    def __init__(self) -> None:
        self.t = 0
        self.n_list = []
        self.input_data = []

    def read_input(self):
        self.t = int(input())
        for i in range(self.t):
            n = int(input())
            line = input().split()
            self.n_list.append(n)
            self.input_data.append([])
            for j in range(n):
                m = int(line[j])
                self.input_data[len(self.input_data) - 1].append(m)

    def solve_case(self, case_input):
        sum = 0
        n = len(case_input)
        arr = [0 for k in range(n)]
        for i in range(1, len(case_input)):
            diff = case_input[i] - case_input[i - 1]
            arr[i] = (2 * arr[i - 1]) % 1000000007 + (diff * (2 ** i - 1)) % 1000000007
        for i in arr:
            sum = (sum + i) % 1000000007
        return sum

    def solve(self):
        for i in range(self.t):
            case_input = self.input_data[i]
            sum = self.solve_case(case_input)
            print(f"Case #{i + 1}: {sum}")

    def print_input(self):
        print(self.t)
        for i in range(self.t):
            n = self.n_list[i]
            print(n)
            for j in range(n):
                print(self.input_data[i][j], end=" ")
            print()


sol = Solution()
sol.read_input()
#sol.print_input()
sol.solve()