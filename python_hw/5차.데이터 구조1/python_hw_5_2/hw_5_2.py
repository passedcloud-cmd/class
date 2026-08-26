# 아래 함수를 수정하시오.
def count_character(text, character):
    """주어진 문자열에서 특정 문자의 개수를 세기"""
    return text.count(character)

result = count_character("Hello, World!", "o")
print(result)  # 2

# 일단 손으로 작성해보자
# text = "Hello, World!"
# print(text.count("o"))
