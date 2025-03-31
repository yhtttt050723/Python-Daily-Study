import json
import re
import os


def clean_ansi_escape(text):
    """清理 ANSI 转义码"""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def extract_decrypted_cast(input_path, output_path):
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"文件 {input_path} 不存在")

        # 读取已解码的 .cast 文件
        with open(input_path, 'r', encoding='utf-8') as f:
            cast_content = f.read()

        # 清理控制字符
        clean_content = clean_ansi_escape(cast_content)

        # 解析 JSON 数据
        events = json.loads(clean_content)

        # 提取所有终端输出事件
        output = []
        for event in events:
            if isinstance(event, list) and len(event) >= 3 and event[1] == 'o':
                output.append(event[2])

        # 保存结果
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(output))

        print(f"成功提取内容到 {output_path}")

    except Exception as e:
        print(f"处理失败: {str(e)}")


if __name__ == "__main__":
    # 输入输出路径配置
    input_file = r"D:\CTFshow misc\download.cast"  # 已解码的文件路径
    output_file = r"D:\CTFshow misc\output.txt"  # 输出文件

    extract_decrypted_cast(input_file, output_file)