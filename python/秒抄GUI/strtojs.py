import streamlit as st
import json

# 初始化一个空字典
data_dict = {}

def correct_input(input_str):
    # 去除输入字符串两边的空格
    input_str = input_str.strip()
    # 分割成多个键值对
    pairs = input_str.split(';')
    corrected_pairs = []
    
    for pair in pairs:
        pair = pair.strip()
        if pair:
            # 分离键和值
            if '=' in pair:
                key, value = pair.split('=', 1)
                # 去除键和值两边的空格，并用双引号包裹
                corrected_key = f'"{key.strip()}"'
                corrected_value = f'"{value.strip()}"'
                corrected_pairs.append(f'{corrected_key}: {corrected_value},')  # 加入逗号
            else:
                st.error(f"键值对格式错误: {pair} 缺少等号。")
                return None
                
    # 拼接成JSON格式的字符串，去除最后一个多余的逗号
    if corrected_pairs:
        corrected_input = '{' + ''.join(corrected_pairs).rstrip(',') + '}'
        return corrected_input
    else:
        return '{}'

def parse_input(input_str):
    try:
        # 尝试解析为JSON格式的字典
        corrected_input = correct_input(input_str)
        if corrected_input is not None:
            parsed_dict = json.loads(corrected_input)
            return parsed_dict
        return None
    except json.JSONDecodeError as e:
        st.error(f"输入格式错误，请检查并重新输入。具体错误: {e}")
        return None

def store_data(input_str):
    """处理存储按钮点击事件，返回更新后的字典"""
    parsed_dict = parse_input(input_str)
    if parsed_dict is not None:
        data_dict.update(parsed_dict)
        return data_dict
    return None
# 按钮点击事件处理
#updated_dict = store_data(user_input)
#if updated_dict is not None:
# 打印更新后的字典
#st.json(updated_dict)
# 将字典存储为JSON文件
#with open('data.json', 'w') as f:
#json.dump(updated_dict, f, indent=4)
#st.success("数据已成功存储！")
