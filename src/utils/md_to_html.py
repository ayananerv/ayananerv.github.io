import os

try:
    from markdown import markdown
except ModuleNotFoundError as e:
    os.system("pip install markdown")
    os.system("pip install python-markdown-math")
    os.system("pip install markdown_checklist")
    from markdown import markdown

try:
    from pymdownx import superfences
except ModuleNotFoundError as e:
    os.system("pip install pymdown-extensions")
    from pymdownx import superfences


class mdtox:
    def __init__(self, md_filename, encoding="utf-8"):
        self.md_filename = md_filename
        self.encoding = encoding
        self.__args()

    def __args(self):
        self.html = """
        <!DOCTYPE html>
        <html lang="en-US">
            <head>
                <meta name="description" content="thanks for 步平凡：https://www.cnblogs.com/bpf-1024/p/14118167.html" />
                <meta charset="utf-8" />
                <meta name="viewpoint" content="width=device-width" />
                <title>{}</title>
                <link rel="stylesheet" href="https://files.cnblogs.com/files/bpf-1024/linenum.css" />
                <link rel="stylesheet" href="https://files.cnblogs.com/files/bpf-1024/markdown.css" />
                <link rel="stylesheet" href="https://files.cnblogs.com/files/bpf-1024/tasklist.css" />
                <link rel="stylesheet" href="https://files.cnblogs.com/files/bpf-1024/codehighlight.css" />
                <link rel="stylesheet" href="https://files.cnblogs.com/files/bpf-1024/directory.css" />
                <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/KaTeX/0.16.8/katex.min.css" crossorigin="anonymous" />
                <script src="https://files.cnblogs.com/files/bpf-1024/directory.js"></script>
                <script src="https://unpkg.com/mermaid@8.7.0/dist/mermaid.min.js"></script>
                <script src="https://cdn.bootcdn.net/ajax/libs/KaTeX/0.16.8/katex.min.js" crossorigin="anonymous"></script>
                <script src="https://cdn.bootcdn.net/ajax/libs/KaTeX/0.16.8/contrib/mathtex-script-type.min.js" defer></script>
                <!-- from ME -->
                <link rel="icon" href="/favicon.ico" type="image/x-icon" />
                <link href="/background.css" rel="stylesheet" type="text/css" />
            </head>
            <body>
                <article class="markdown-body" id="markdown-body">
                    {}
                </article>
            </body>
        </html>
        """

        # 扩展配置
        self.extensions = [
            "toc",  # 目录，[toc]
            "extra",  # 缩写词、属性列表、释义列表、围栏式代码块、脚注、在HTML的Markdown、表格
        ]
        third_party_extensions = [
            "mdx_math",  # KaTeX数学公式，$E=mc^2$和$$E=mc^2$$
            "markdown_checklist.extension",  # checklist，- [ ]和- [x]
            "pymdownx.magiclink",  # 自动转超链接，
            "pymdownx.caret",  # 上标下标，
            "pymdownx.superfences",  # 多种块功能允许嵌套，各种图表
            "pymdownx.betterem",  # 改善强调的处理(粗体和斜体)
            "pymdownx.mark",  # 亮色突出文本
            "pymdownx.highlight",  # 高亮显示代码
            "pymdownx.tasklist",  # 任务列表
            "pymdownx.tilde",  # 删除线
        ]
        self.extensions.extend(third_party_extensions)
        self.extension_configs = {
            "mdx_math": {"enable_dollar_delimiter": True},  # 允许单个$
            "pymdownx.superfences": {
                "custom_fences": [
                    {
                        "name": "mermaid",  # 开启流程图等图
                        "class": "mermaid",
                        "format": superfences.fence_div_format,
                    }
                ]
            },
            "pymdownx.highlight": {
                "linenums": True,  # 显示行号
                "linenums_style": "pymdownx-inline",  # 代码和行号分开
            },
            "pymdownx.tasklist": {
                "clickable_checkbox": True,  # 任务列表可点击
            },
        }

    def to_html(self, html_name):
        try:
            with open(self.md_filename, "r", encoding=self.encoding) as file_md:
                md_text = file_md.read()
        except Exception as e:
            print("<Error>", e)
            return False

        title = ".".join(os.path.basename(self.md_filename).split(".")[:-1])
        html_text = markdown(
            md_text,
            output_format="html",
            extensions=self.extensions,
            extension_configs=self.extension_configs,
        )  # MarkDown转HTML
        self.html = self.html.format(title, html_text)

        try:
            with open(html_name, "w", encoding=self.encoding) as file_html:
                file_html.write(self.html)
        except Exception as e:
            print("<Error>", e)
            return False

        return True


# 本测试与上述代码在同个文件中
if __name__ == "__main__":
    md_name = input("请输入md文件名：")
    html_name = input("请输入html文件名：")

    if mdtox(md_name).to_html(html_name):
        print("转换完成")
