import os
from mutagen.flac import FLAC

#读取FLAC文件
def read_cover(file_path,output_path = None):
    try:
        file = FLAC(file_path)#找到把文件定义为file 未找到抛出错误
    except Exception as e:
        print(f'未找到文件:{e}')
        return

    #检查是否有图片
    if not file.pictures:
        print('文件中没有封面')
        return

    #如果有 获取第一张图片
    picture = file.pictures[0]

    #在未指定文件名时 确定输出的文件名
    if output_path is None:
        ext = '.jpg' if picture.mime == 'image/jpeg' else '.png'
        '''
        根据 FLAC 文件中嵌入图片的 MIME 类型（picture.mime）决定扩展名：
        若 MIME 类型是 image/jpeg → 扩展名为 .jpg。
        若 MIME 类型是其他（如 image/png）→ 扩展名为 .png。
        潜在问题：
        如果图片的实际格式与 MIME 类型不匹配（例如 MIME 是 image/webp），扩展名会错误地设为 .png，导致文件无法正确打开。
        '''
        #输出路径设置
        output_path = os.path.splitext(file_path)[0] + ext
        #os.path.splittext 作用是可以将路径拆解成 （文件名，拓展名）取第一位加上文件尾组成最终文件名

    try:
        with open(output_path,'wb') as img_file:#wb 以二进制写入模式打开文件
            img_file.write(picture.data)#将提取图片的二进制数据写入文件
            print(f'封面已提取并保存为：{output_path}')
    except Exception as e:
        print(f'写入失败:{e}')
if __name__ == '__main__':
    flac = r'D:\CTFshow misc\task.flac'#这里要改成自己文件路径
    read_cover(flac)
