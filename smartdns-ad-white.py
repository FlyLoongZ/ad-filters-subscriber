import re

# 指定输入文件的路径
input_file_path = "./rule/adblock.txt"
# 指定输出文件的路径
output_file_path = "./rule/smartdns-ad-white.txt"

# 正则表达式模式，用于匹配以 @@|| 开头，后跟任意字符（非贪婪），直到遇到 ^ 或 ^| 或 \n
url_pattern = re.compile(r'@@\|\|(.*?)(\^|\^\||\n)', re.MULTILINE)

try:
    # 打开输入文件并读取内容
    with open(input_file_path, 'r') as file:
        text = file.read()

    # 使用正则表达式查找所有匹配的网址
    urls = url_pattern.findall(text)

    # 将提取的网址写入到输出文件中
    with open(output_file_path, 'w') as file:
        for url_tuple in urls:
            # 提取第一个捕获组的内容（真正的网址主体部分）
            clean_url = url_tuple[0]
            # 判断第二个捕获组是否匹配到了 ^，如果是，去除多余的 ^
            if url_tuple[1] == '^':
                clean_url = clean_url.rstrip('^')
            file.write(clean_url + '\n')

    print(f'网址已成功写入到文件 {output_file_path} 中。')
except FileNotFoundError:
    print(f'文件 {input_file_path} 未找到，请检查路径是否正确。')
except Exception as e:
    print(f'发生错误：{e}')
