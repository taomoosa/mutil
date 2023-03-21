def replace_numbers(input_string):
    """
    入力文字列のうち、[]で囲われた整数を-1した値に置換した文字列を返す。

    Args:
        input_string (str): 入力文字列。

    Returns:
        str: []で囲われた整数が-1した値に置換された文字列。
    """
    import re
    
    # 正規表現パターンの定義
    pattern = r'\[(\d+)\]'
    
    # 正規表現による置換処理
    output_string = re.sub(pattern, lambda m: '[' + str(int(m.group(1))-1) + ']', input_string)
    
    return output_string

print(replace_numbers("a[1].b[2][111]"))