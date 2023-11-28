这是Linux第三次实验，关于shell命令的操作；共有4道题目。现稍作整理：

**！！！有不确定、不正确的地方！！！**

----

1. 使用`echo`命令输出以下内容：
   + Hello world
   + Hello

     world
   + "Hello world"
   + ?'*[]&();>"<

   **Answer:**
    ```shell
    #!/bin/bash

    echo "Hello world"

    echo "Hello\nworld"

    echo "\"Hello world\""

    echo "?'*[]&();>\"<"
    ```

----

2. shell变量：
   + 创建变量`name`，赋值为自己姓名字母缩写。
   + 显示变量`name`的值。
   + 修改shell变量提示符使之显示命令序号。
   + 为`rm -i`创建别名`del`。

   **Answer:**
   ```shell
   #!/bin/bash

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

   **Answer**
   ```shell
   #!/bin/bash

   vi .profile

   # ~/.profile
   some commands...
   echo "Hello $USER"
   echo "Current Date & Time: $(date)"
   ~
   ~
   ```

----

4. 进程管理：
   + 创建后台进程`vi numbers`，查看其ID。
   + 终止该后台进程。

   **Answer:**
   ```shell
   #!/bin/bash

   vi numbers &
   ps
   ```

----

5. 创建一个shell脚本sum，要求如下：
   + 使用方法是`$ sum a b`，其中a、b是两个整数，且a < b；
   + 功能是计算a到b的累加和；
   + 终端输出 `a+...+b=累加和`
   + 例如：`sum 3 5` 输出 `3+...+5=12`

   **Answer:**
   ```shell
   #!/bin/bash

   s=0

   for((i=$1;i<=$2;i++))
   do
     s=$[$s+$i]
   done

   echo "$1+...+$2=$s"
   ```