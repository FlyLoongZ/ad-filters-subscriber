import re

# 指定输入文件的路径
input_file_path = "./rule/adblock.txt"
# 指定输出文件的路径
output_file_path = "./rule/smartdns-ad.txt"

# 正则表达式模式，用于匹配以 || 开头，后跟任意字符（非贪婪），直到遇到 ^
url_pattern = re.compile(r'^\|\|(.*?)\^$', re.MULTILINE)

try:
    # 打开输入文件并读取内容
    with open(input_file_path, 'r') as file:
        text = file.read()

    # 使用正则表达式查找所有匹配的网址
    urls = url_pattern.findall(text)

    # 将提取的网址写入到输出文件中
    with open(output_file_path, 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print(f'网址已成功写入到文件 {output_file_path} 中。')
except FileNotFoundError:
    print(f'文件 {input_file_path} 未找到，请检查路径是否正确。')
except Exception as e:
    print(f'发生错误：{e}')