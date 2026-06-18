import json
from collections import OrderedDict

class SiteSummary:
    def __init__(self, data):
        self.data = data

    def generate_summary(self):
        summary_lines = []
        for item in self.data:
            name = item.get("site_name", "未知站点")
            url = item.get("site_url", "")
            keywords = item.get("keywords", [])
            tags = item.get("tags", [])
            description = item.get("description", "")
            summary_lines.append(f"站点名称: {name}")
            summary_lines.append(f"网址: {url}")
            summary_lines.append(f"关键词: {'、'.join(keywords)}")
            summary_lines.append(f"标签: {'、'.join(tags)}")
            summary_lines.append(f"说明: {description}")
            summary_lines.append("-" * 40)
        return "\n".join(summary_lines)

def load_site_data():
    sample_data = [
        OrderedDict({
            "site_name": "开云官方网站",
            "site_url": "https://position-kaiyun.com.cn",
            "keywords": ["开云", "体育", "娱乐"],
            "tags": ["体育平台", "娱乐", "在线"],
            "description": "提供体育赛事、电子竞技等多种娱乐服务的平台。"
        }),
        OrderedDict({
            "site_name": "开云资讯",
            "site_url": "https://position-kaiyun.com.cn/news",
            "keywords": ["开云", "新闻", "资讯"],
            "tags": ["新闻", "体育", "动态"],
            "description": "获取开云平台最新动态与行业资讯。"
        }),
        OrderedDict({
            "site_name": "开云帮助中心",
            "site_url": "https://position-kaiyun.com.cn/help",
            "keywords": ["开云", "帮助", "支持"],
            "tags": ["帮助", "客服", "指南"],
            "description": "提供常见问题解答与客户支持服务。"
        })
    ]
    return sample_data

def format_summary_to_json(summary_text):
    lines = summary_text.strip().split("\n")
    entries = []
    current_entry = {}
    for line in lines:
        if line.startswith("站点名称:"):
            if current_entry:
                entries.append(current_entry)
                current_entry = {}
            current_entry["站点名称"] = line.split(":", 1)[1].strip()
        elif line.startswith("网址:"):
            current_entry["网址"] = line.split(":", 1)[1].strip()
        elif line.startswith("关键词:"):
            current_entry["关键词"] = line.split(":", 1)[1].strip()
        elif line.startswith("标签:"):
            current_entry["标签"] = line.split(":", 1)[1].strip()
        elif line.startswith("说明:"):
            current_entry["说明"] = line.split(":", 1)[1].strip()
    if current_entry:
        entries.append(current_entry)
    return json.dumps(entries, ensure_ascii=False, indent=2)

def main():
    site_data = load_site_data()
    summarizer = SiteSummary(site_data)
    summary_text = summarizer.generate_summary()
    print("结构化摘要（文本）:")
    print(summary_text)
    print("\n结构化摘要（JSON）:")
    json_output = format_summary_to_json(summary_text)
    print(json_output)

if __name__ == "__main__":
    main()