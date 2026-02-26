"""
学生信息管理系统 - 数据操作模块
包含：将数据写入json文件save_data(data)、从json读取数据load_data()
日期：2026-02-26
"""

import json

def save_data(data):
    """写入文件"""
    with open("student_data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)

def load_data():
    """读取文件"""
    try:
        with open("student_data.json", "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}