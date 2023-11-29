import os


class my_structure:
    def __init__(self, html_name, encoding="utf-8") -> None:
        self.html_name = html_name
        self.encoding = encoding
        self.__args()
        pass

    def __args(self):
        self.html = """
        <!DOCTYPE html>
        <html lang="en-US">

        <head>
          <meta charset="utf-8" />
          <meta name="viewpoint" content="width=device-width" />
          <!-- from ME -->
          <link rel="icon" href="/favicon.ico" type="image/x-icon" />
          <link href="/background.css" rel="stylesheet" type="text/css" />
        </head>

        <body>
          <header>

          </header>

          <nav>

          </nav>

          <main>
            <article>

            </article>

            <aside>

            </aside>

          </main>

          <footer>

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
