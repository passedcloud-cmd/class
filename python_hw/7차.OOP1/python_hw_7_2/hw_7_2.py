# 아래 클래스를 수정하시오.

# 주어진 문자열을 반복출력하는 클래스를 만들기
# 반복 횟수와 문자열을 인자로 받아 문자열을 반복 출력하는 repeat_string 메서드가 포함되어야 함

class StringRepeater:
    def __init__(self, step = 0, string =0):
        self.step = step
        self.string = string

    def repeat_string(self, step, string):
        self.repeat = step * (string + "\n")
        print(self.repeat)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

# 문제점
# def __init__(self, step = 0, string =0)로 두면
# self.step과 self.string을 안 쓰고 버리는 것. 불필요한 반복이 있는 것.




# class StringRepeater:
#     def __init__(self, step, string):
#         self.step = step
#         self.string = string

#     def repeat_string(self):
#         self.repeat = self.step * (self.string + "\n")
#         print(self.repeat)

# repeater1 = StringRepeater(3, "Hello")
# repeater1.repeat_string()