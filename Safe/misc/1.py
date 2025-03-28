
import os
from mutagen.flac import FLAC
def extract_flac_cover(flac_file_path, output_image_path=None):
        # 加载FLAC文件
    try:
        audio = FLAC(flac_file_path)
    except Exception as e:
        print(f"无法读取 FLAC 文件: {e}")
        return
        # 检查是否有图片
    if not audio.pictures:
        print("该 FLAC 文件中未找到封面图像。")
        return
        # 获取第一张图片
    picture = audio.pictures[0]
        # 确定输出文件名
    if output_image_path is None:
        ext = ".jpg" if picture.mime == "image/jpeg" else ".png"
        output_image_path = os.path.splitext(flac_file_path)[0] + ext
        # 写入图片文件
    try:
        with open(output_image_path, "wb") as img_file:
            img_file.write(picture.data)
        print(f"封面已提取并保存为: {output_image_path}")
    except Exception as e:
        print(f"写入图片文件失败: {e}")
if __name__ == "__main__":
    flac_path = r'D:\CTFshow misc\task.flac'
    extract_flac_cover(flac_path)