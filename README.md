# 智能客服系统

## 项目概述

此项目实现了一个简单的智能客服系统，主要利用 OpenAI 的嵌入模型将客服相关文本数据转换为向量，并通过 FAISS 向量数据库进行相似文本搜索。系统基于 Python 和 LangChain 家族库构建，适合用于演示如何快速构建基于语义搜索的问答系统。

## 功能特点

- **数据加载**：模拟加载 FAQ、产品介绍、工作时间、退换货政策等客服文本数据。
- **向量存储构建**：使用 OpenAI 嵌入模型生成文本向量，并借助 FAISS 构建向量数据库，实现高效相似度搜索。
- **相似度查询**：根据用户输入查询最匹配的文本，返回预设的回答。
- **交互式命令行**：提供简单的命令行交互界面，用户可以通过输入问题获得答案，输入 `退出` 或 `exit` 结束对话。

## 项目结构

- `app.py`：主程序文件，包含程序的主要逻辑 —— 文本加载、向量数据库构建、查询处理以及基于 Flask 的交互式问答 Web UI。
- `requirements.txt`：依赖包清单，安装这些包后即可运行项目。

## 环境要求

- Python 3.7 或更高版本。
- 已配置 OpenAI API 密钥。请确保设置了环境变量 `OPENAI_API_KEY`（用于 OpenAI 的 API 调用），例如：
  ```bash
  export OPENAI_API_KEY="your_openai_api_key_here"
  ```

## 安装步骤

1. **克隆项目**
   ```bash
   git clone <项目仓库地址>
   cd <项目仓库目录>
   ```

2. **创建虚拟环境（推荐）**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 用户请使用：venv\Scripts\activate
   ```

3. **安装项目依赖**
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

运行项目 Web 应用：

```bash
python app.py
```

程序启动后，请在浏览器中访问 [http://localhost:5000](http://localhost:5000)，即可使用基于 Web 的交互式界面进行问答。

## 常见问题

**Q: 如何获取 OpenAI API 密钥？**  
A: 请访问 [OpenAI 官网](https://openai.com/api/) 注册账号并获取 API 密钥，然后设置环境变量 `OPENAI_API_KEY`。

**Q: 项目如何扩展？**  
A: 目前的系统仅采用简单的相似度匹配技术。您可以结合大语言模型（LLM）生成更复杂的回答，或者整合更多数据源以提高响应质量。

## 贡献与反馈

欢迎对本项目进行改进和扩展。如果您有任何问题或建议，请通过 Issue 或直接提交 Pull Request。

## 许可证

本项目遵循 MIT 许可证。详细信息请参见 [LICENSE](LICENSE) 文件（如果存在）。