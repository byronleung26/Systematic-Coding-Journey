# app.py - 运行这个文件
from flask import Flask, render_template_string, request
import random
from datetime import datetime

app = Flask(__name__)

# HTML模板（简单美观）
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>除夕快乐！</title>
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Microsoft YaHei', sans-serif;
            margin: 0;
            padding: 20px;
        }
        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }
        h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .year {
            color: #764ba2;
            font-size: 1.5em;
            margin-bottom: 30px;
        }
        .greeting {
            background: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            font-size: 1.3em;
            color: #333;
            border-left: 5px solid #667eea;
        }
        input {
            width: 80%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 1em;
            margin: 10px 0;
        }
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 10px;
            font-size: 1.1em;
            cursor: pointer;
            transition: transform 0.2s;
            margin: 10px;
        }
        button:hover {
            transform: scale(1.05);
        }
        .footer {
            margin-top: 30px;
            color: #666;
            font-size: 0.9em;
        }
        .firework {
            font-size: 2em;
            animation: twinkle 1s infinite;
        }
        @keyframes twinkle {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="firework">🎆 🧨 ✨</div>
        <h1>除夕快乐！</h1>
        <div class="year">2026 丙午马年</div>
        
        <form method="POST">
            <input type="text" name="name" placeholder="输入朋友的名字" required>
            <br>
            <button type="submit" name="action" value="generate">生成专属祝福 🎁</button>
            <button type="submit" name="action" value="random">随机祝福 🎲</button>
        </form>
        
        {% if greeting %}
        <div class="greeting">
            {{ greeting }}
        </div>
        {% endif %}
        
        <div class="footer">
            ⚡ 用Python Flask开发的第一个Web应用<br>
            🧧 祝大家新年快乐，代码无bug！
        </div>
    </div>
</body>
</html>
'''

# 祝福语库
BLESSINGS = [
    "{}，新年快乐！愿你代码写得顺，Bug找得快，需求改得少，年终奖拿得多！",
    "{}，祝你新的一年：Flask/Django都会，前端后端都对，涨薪升职都行！",
    "{}，2026马年大吉！愿你的代码如骏马奔腾，Bug都望尘莫及！",
    "{}，除夕快乐！祝你学Web开发不走弯路，找工作不走回头路！",
    "{}，新年到！愿你：Flask用得溜，Django学得快，月薪过万不是梦！",
    "{}，马年吉祥！祝你像千里马一样，遇到赏识你的伯乐（老板）！",
    "{}，新的一年，愿你：Git不冲突，部署不出错，需求不反复！",
    "{}，除夕夜还在看Python的你，一定会成为最牛的Web开发者！"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = None
    
    if request.method == 'POST':
        name = request.form.get('name', '朋友')
        action = request.form.get('action')
        
        if action == 'random':
            # 随机生成祝福语
            greeting = random.choice(BLESSINGS).format(name)
        else:
            # 生成一个固定的祝福
            greeting = f"{name}，除夕快乐！愿你2026年Python技术飞升，Web开发之路一帆风顺！"
    
    return render_template_string(HTML_TEMPLATE, greeting=greeting)

if __name__ == '__main__':
    print("🎉 新年祝福应用已启动！")
    print("📱 在浏览器打开: http://127.0.0.1:5000")
    print("🔧 按 Ctrl+C 退出")
    app.run(debug=True)