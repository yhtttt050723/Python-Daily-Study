import pandas as pd
from openai import OpenAI
import os
from tqdm import tqdm
import re

# ----------------------
# DeepSeek API 配置
# ----------------------
client = OpenAI(
    api_key="sk-76b8a787d6a24036bba4b27db01fea3a",  # 替换真实API密钥
    base_url="https://api.deepseek.com/v1",
)


# ----------------------
# 大模型判断函数
# ----------------------
def get_deepseek_judgement(prompt):
    """调用 DeepSeek API 获取判断"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return response.choices[0].message.content.strip().lower()
    except Exception as e:
        print(f"API 错误: {e}")
        return "error"


# ----------------------
# 判断逻辑（新增三个条件）
# ----------------------
def requires_context(row):
    """判断是否需要上下文才能回答问题"""
    prompt = f"""请判断以下问题是否需要依赖上下文才能正确回答，只需回答 yes/no：
    问题：{row['question_translated']}
    当前答案：{row['concise_answer_translated']}"""
    return get_deepseek_judgement(prompt) == "yes"


def is_answer_wrong(row):
    """判断答案是否完全错误"""
    prompt = f"""请严格判断以下答案是否完全错误或未回答问题，只需回答 yes/no：
    问题：{row['question_translated']}
    答案：{row['concise_answer_translated']}"""
    return get_deepseek_judgement(prompt) == "yes"


def has_chart_in_column_f(content):
    """检查 complete_context 列是否包含图表关键词"""
    # 定义图表关键词（可根据数据特点补充）
    chart_keywords = ['图', '表', 'chart', 'figure', '图像', '插图', '图片']
    content = str(content).lower()
    return any(keyword in content for keyword in chart_keywords)


# ----------------------
# 筛选流程（三步删除）
# ----------------------
def filter_dataframe(df):
    # 条件1：删除需要上下文的回答
    print("正在删除需要上下文的问题...")
    tqdm.pandas(desc="上下文检查")
    df = df[~df.progress_apply(requires_context, axis=1)]

    # 条件2：删除完全错误的答案
    print("\n正在删除错误答案...")
    tqdm.pandas(desc="错误检查")
    df = df[~df.progress_apply(is_answer_wrong, axis=1)]

    # 条件3：删除包含图表的问题（直接操作列，无需逐行API调用）
    print("\n正在删除包含图表的问题...")
    df = df[~df['complete_context'].apply(has_chart_in_column_f)]

    return df


# ----------------------
# 执行流程
# ----------------------
if __name__ == "__main__":
    # 加载数据
    df = pd.read_excel(r"C:\Users\闫鹤天\Desktop\2.xlsx", engine='openpyxl')

    # 执行筛选
    filtered_df = filter_dataframe(df)

    # 保存结果
    filtered_df.to_csv("filtered_output.csv", index=False)
    print(f"处理完成！原始数据：{len(df)}条 → 筛选后：{len(filtered_df)}条")