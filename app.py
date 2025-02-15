import os
from flask import Flask, render_template_string, request
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# 配置 OpenAI 接口参数（根据实际情况调整域名）
openai.api_base = "https://api.openai-hk.com/v1"
openai.base_url = "https://api.openai-hk.com/v1"
openai.api_key = os.environ["OPENAI_API_KEY"]

def load_texts():
    """
    模拟加载客服相关文本数据
    """
    return [
        "欢迎使用我们的客服系统，我们随时为您服务。",
        "我们提供A、B、C等多种产品，具体详情请参考产品说明。",
        "我们的工作时间为周一到周五，早上9点至下午6点。",
        "如遇技术问题，请联系技术支持团队。",
        "退换货政策为购买后三十天内办理。"
    ]

def build_vector_storage(texts):
    """
    利用 OpenAI 嵌入模型构建向量存储（FAISS）
    """
    embeddings = OpenAIEmbeddings()  # 会从环境变量中读取 OPENAI_API_KEY
    vector_db = FAISS.from_texts(texts, embeddings)
    return vector_db

def process_query(query, vector_db):
    """
    根据用户输入查询最匹配的文本作为回答依据
    """
    results = vector_db.similarity_search(query)
    if results:
        return results[0].page_content
    else:
        return "抱歉，我没有找到相关信息，请再次尝试其他问题。"

# 在服务器启动时加载文本并构建向量数据库
texts = load_texts()
vector_db = build_vector_storage(texts)

app = Flask(__name__)

# 内联 HTML 模板，用于显示问答界面
HTML_TEMPLATE = """
<!doctype html>
<html lang="zh">
<head>
    <meta charset="utf-8">
    <title>智能客服系统</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background-color: #f4f4f4; }
        .chat-box { background: #fff; border: 1px solid #ccc; padding: 20px; width: 100%; max-width: 100%; box-shadow: 2px 2px 12px rgba(0,0,0,0.1); }
        .message { padding: 10px; margin: 5px 0; border-radius: 5px; }
        .user { background-color: #e0f7fa; text-align: left; }
        .bot { background-color: #dcedc8; text-align: left; }
        .input-box { width: 80%; padding: 10px; }
        .send-btn { padding: 10px 20px; }
    </style>
</head>
<body>
    <div class="chat-box">
        <h2>智能客服系统</h2>
        <div id="chat">
            {% for message in messages %}
                <div class="message {{ message.sender }}">
                    <strong>{{ '您' if message.sender == 'user' else '客服' }}:</strong> {{ message.text }}
                </div>
            {% endfor %}
        </div>
        <form action="/" method="POST">
            <input type="text" name="query" class="input-box" placeholder="请输入您的问题" autofocus autocomplete="off" required>
            <button type="submit" class="send-btn">发送</button>
        </form>
    </div>
</body>
</html>
"""

# 简单使用一个全局变量保存对话记录（生产环境建议使用 session 或数据库持久化）
conversation = []

@app.route("/", methods=["GET", "POST"])
def index():
    global conversation
    if request.method == "POST":
        user_query = request.form.get("query")
        if user_query:
            # 添加用户消息到对话中
            conversation.append({"sender": "user", "text": user_query})
            # 处理问题获取回答
            response = process_query(user_query, vector_db)
            conversation.append({"sender": "bot", "text": response})
    return render_template_string(HTML_TEMPLATE, messages=conversation)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 