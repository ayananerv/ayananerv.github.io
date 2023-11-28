这是Linux第三次实验，关于shell命令的操作；共有4道题目。现稍作整理：

**！！！有不确定、不正确的地方！！！**

----

1. 使用echo命令输出以下内容：
   + Hello world
   + Hello

     world
   + "Hello world"
   + ?'*[]&();>"<

   **Answer:**
    ```shell
    echo "Hello world"

    echo "Hello\nworld"

    echo "\"Hello world\""

    echo "?'*[]&();>\"<"
    ```

----

2. shell变量：
   + 创建变量name，赋值为自己姓名字母缩写。
   + 显示变量name的值。
   + 修改shell变量提示符使之显示命令序号。
   + 为rm -i创建别名del。

   **Answer:**
   ```shell
   name=ljz

   echo $name

   PS1="\#"

   alias del="rm -i"
   # also available:
   alias del='rm -i'
   ```

----

3. 登陆配置文件：
   + 修改.profile文件，以便每次登陆时显示如下信息：（xxx分别为你的用户名和当前时间，精确到秒）

     Hello xxx

     Current Date & Time: xxx

----

4. 进程管理：
   + 创建后台进程vi numbers，查看其ID。
   + 终止该后台进程。


----

5. 创建一个shell脚本sum，要求如下：
   + 使用方法是$ sum a b，其中a、b是两个整数，且a < b；
   + 功能是计算a到b的累加和；
   + 终端输出 a+...+b=累加和
   + 例如：sum 3 5 输出 3+...+5=12

