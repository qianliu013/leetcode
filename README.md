# LeetCode solutions

## 结构说明

- common 放用于一些 LeetCode 代码运行需要的 package，如 TreeNode，ListNode 和用于测试的 test_tools.py
- 文件夹用难度分类，名称为题号
- easy 难度全部用 python 而写，但大部分代码很容易稍微改动成其他语言的形式

## 文件内容说明

### python 文件

- LeetCode 自动生成的格式（类）太麻烦，因此简化了一下

  - 大部分都用一个 `_solve` 来表示最终的 solution
  - `_solve` 舍去了LeetCode 自动生成的类的函数第一个参数 `self`, 其参数为原来的第二个到最后一个，参数名不变
  - 一些题目用了闭包的方法来避免使用类
  - 一些必须用类的保持依旧使用类
  - `_solve`, `_solve1` 等代表不同方式的 solution
  - 提交 LeetCode 运行的时候仅需提交函数后的一部分，注意缩进

- 大部分 solution 下都包含几种题解
  - 一般第一（或包含第二）个解法是自己思考后 Accepted 的解法
  - 其后的部分整理改编自 discuss 中高票的内容

- 一些内容说明
  - 名字前加 `_` 和 `__` 遵循 pep8（使用 pylint 检查规范）