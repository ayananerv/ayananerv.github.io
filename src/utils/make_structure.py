import os


class my_structure:
    def __init__(self, html_name, encoding="utf-8") -> None:
        self.html_name = html_name
        self.encoding = encoding
        self.__args()
        pass

    def __args(self):
        self.html = """<!DOCTYPE html>
<html lang="en-US">

<head>
  <meta charset="utf-8" />
  <meta name="viewpoint" content="width=device-width" />
  <!-- from ME -->
  <link rel="icon" href="/favicon.ico" type="image/x-icon" />
  <link href="/background.css" rel="stylesheet" type="text/css" />
  <title>give me a title</title>
</head>

<body>
    <header>
    <h1>未来在过去之前</h1>
    <h2>THE FUTURE LIES IN THE PAST OF THE PAST</h2>
  </header>


  <div>
    <p>想通过这个网站记录一些专业上的知识、自己感兴趣的小说、想法和音乐等。（施工中...）</p>
  </div>

  <hr>

  <nav>
    <p>导航栏</p>
    <ul>
      <li><a href="hyper-reference">name</a></li>
    </ul>
  </nav>

  <hr>



  <main>
    <article>

    </article>

    <aside>

    </aside>

  </main>

  <hr>

  <footer>
    <!-- 本站所有网页的统一页脚 -->
    <p>© 2023 ME保留所有权利</p>
  </footer>
</body>

</html>
        """

    def make_structure(self):
        try:
            with open(self.html_name, "w") as f:
                f.write(self.html)
        except Exception as e:
            print("<Error>", e)
            return False

        return True


if __name__ == "__main__":
    html_name = input("请输入新建html文件名：")

    if my_structure(html_name).make_structure():
        print("结构化成功")
