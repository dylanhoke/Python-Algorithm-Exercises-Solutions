def solution(inputString):
    def reverse_inner_parentheses(substring):
        open_index = substring.rfind('(')
        close_index = substring.find(')', open_index)

        if open_index != -1 and close_index != -1:
            between_parentheses = substring[open_index + 1:close_index]
            reversed_values = between_parentheses[::-1]
            return (
                substring[:open_index] +
                reversed_values +
                substring[close_index + 1:]
            )
        else:
            return substring

    result = inputString

    while '(' in result and ')' in result:
        result = reverse_inner_parentheses(result)

    return result