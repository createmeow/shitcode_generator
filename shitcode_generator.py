import os
import re

def generate_shitcode():
    file_path = "shitcode.py"
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 创建初始文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('while True:\n')
            f.write('    输入 = input("请输入一个数值: ")\n')
            f.write('    try:\n')
            f.write('        数值 = int(输入)\n')
            f.write('        if 数值 == 1:\n')
            f.write('            print("是奇数")\n')
            f.write('        elif 数值 == 2:\n')
            f.write('            print("是偶数")\n')
            f.write('        else:\n')
            f.write('            print("请输入1-2之间的数值")\n')
            f.write('    except ValueError:\n')
            f.write('        print("请输入有效的数值")\n')
        print("已创建初始shitcode.py文件")
    else:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分析当前最大数值
        pattern = r'数值 == (\d+)' 
        matches = re.findall(pattern, content)
        if matches:
            max_num = max(map(int, matches))
        else:
            max_num = 2
        
        # 生成新的代码
        new_code = ''
        for i in range(max_num + 1, max_num + 4):  # 每次添加3个数值
            if i % 2 == 1:
                new_code += f'        elif 数值 == {i}:\n            print("是奇数")\n'
            else:
                new_code += f'        elif 数值 == {i}:\n            print("是偶数")\n'
        
        # 替换else语句
        updated_content = re.sub(r'        else:\n            print\("请输入1-\d+之间的数值"\)\n', 
                               new_code + f'        else:\n            print("请输入1-{max_num + 3}之间的数值")\n', 
                               content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"已更新shitcode.py文件，添加了{max_num + 1}到{max_num + 3}的判断")

import time

if __name__ == "__main__":
    print("史山代码生成器启动")
    print("按Ctrl+C退出")
    try:
        while True:
            generate_shitcode()
            # 自动等待1秒后继续生成
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n生成器已退出")
