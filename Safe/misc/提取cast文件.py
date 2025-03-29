import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import re


def decrypt_cast(encrypted_data):
    """AES-CBC解密函数"""
    key = b'__ELPSYCONGROO__'  # 16字节密钥
    iv = b'114_514_1919_810'  # 16字节IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_data)
    return unpad(decrypted, AES.block_size)


def clean_ansi_escape(text):
    """清理ANSI转义码"""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def extract_cast_content(input_file, output_file):
    try:
        # 读取文件内容
        with open(input_file, 'rb') as f:
            raw_data = f.read()

        # 尝试解密（适用于加密文件）
        try:
            decrypted_data = decrypt_cast(raw_data)
            cast_content = decrypted_data.decode('utf-8')
        except (ValueError, UnicodeDecodeError):
            # 如果解密失败，直接尝试作为JSON读取
            cast_content = raw_data.decode('utf-8')

        # 解析JSON内容
        events = json.loads(cast_content)

        # 提取所有输出内容
        output = []
        for event in events:
            if len(event) >= 3 and event[1] == 'o':  # 格式：[时间, 类型, 内容]
                output.append(event[2])

        # 合并内容并清理控制字符
        full_text = clean_ansi_escape(''.join(output))

        # 保存结果
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_text)

        print(f"成功提取内容到 {output_file}")

    except Exception as e:
        print(f"处理失败: {str(e)}")


if __name__ == "__main__":
    input_file = r"D:\CTFshow misc\record.cast"  # 输入文件名
    output_file = r"D:\CTFshow misc\output.txt"  # 输出文件名
    extract_cast_content(input_file, output_file)