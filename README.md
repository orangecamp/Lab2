# 日志型数据库的基础

## 学习目标

- 掌握 Python 制作一个简单 CLI 程序的能力
- 学习并使用 Python 序列化 json 的知识
- 学会 Python 文件相关操作（读写）
- 知晓 CLI 是其它程序与用户调用该程序的接口
- 对文件的知识有所了解

## 项目介绍

日志型符号表是一些数据库的底层实现，我们今天的项目即为编写一个小型的更简单的这种日志型数据表，原型来自 [bitcask](https://github.com/basho/bitcask) 。

## 项目目标

请补全 `main.py` 里的 `main` 函数。

你需要在 `data` 目录下创建一个 `store.kv` 文件来储存键值对数据。程序每次启动时，你需要从这里读取响应的数据并载入程序中。
请自定义文件里的内容，你需要运用到序列化的知识，选择何种序列化，JSON或其它自定义格式由你决定。

你需要使用 `argparse` 或其它命令行模块实现这三个 CLI 指令。


### Set 指令 

格式如下: `set <KEY> <VALUE>`

将 <KEY> 的值设置为 <VALUE>

然后将这个操作序列化为一个 String，输出到 `store.kv` 里。

### Get 指令 
格式如下: `get <KEY>`

打印 <KEY> 的值，不存在则输出 `Key not found`

### Del 指令 
格式如下: `del <KEY>`

删除 <KEY> 的值，不存在则输出 `Key not found`

然后将这个操作序列化为一个 String，输出到 `store.kv` 里。

### 样例输入

```sh
python -m src.log_structured_file_io.main set a 1
python -m src.log_structured_file_io.main get a
python -m src.log_structured_file_io.main get b
```

### 样例输出

```
1
Key not found
```


## 样例测试

你可以通过输入 `pdm run pytest` 来检测代码运行结果

## 其它要求

- 请独立完成项目的编写，不要与他人交流
- 请不要借助 AI 编写代码


## 致谢
- 原型项目：PingCAP [talent-plan-rust-project-2](https://github.com/pingcap/talent-plan/tree/master/courses/rust/projects/project-2)
