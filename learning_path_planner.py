import qianfan
import os

# 本地运行时在系统环境变量里填入你的 AccessKeyID / SecretAccessKey
os.environ["QIANFAN_ACCESS_KEY"] = "你的AccessKeyID"
os.environ["QIANFAN_SECRET_KEY"] = "你的SecretAccessKey"

def generate_learning_path(topic, level, time_budget):
    print(f"\n正在连接百度 AI，正在为《{topic}》定制学习方案，请稍候...\n")

    try:
        resp = qianfan.ChatCompletion().do(
            model="ERNIE-Bot-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    你是一位资深导师。请为一个{level}水平的人，制定一份学习{topic}的计划。
                    要求：
                    1. 分阶段（基础、进阶、实战）。
                    2. 给出核心知识点和推荐练习方式。
                    3. 时间限制：{time_budget}。
                    4. 请用 Markdown 格式输出，包含表格。
                    """
                }
            ]
        )
        return resp['result']

    except Exception as e:
        return f"调用失败: {str(e)}"


def main():
    print("👋 欢迎使用个性化学习路径规划师")
    print("-" * 40)
    topic = input("1. 请输入你想学习的主题: ")
    level = input("2. 请输入你的当前水平: ")
    time_budget = input("3. 你每天/每周能投入多少时间？: ")
    plan = generate_learning_path(topic, level, time_budget)
    print("\n" + "=" * 40)
    print("🚀 你的专属学习路径已生成：")
    print("=" * 40)
    print(plan)
    print("=" * 40)

if __name__ == "__main__":
    main()