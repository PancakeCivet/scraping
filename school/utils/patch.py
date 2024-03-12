import subprocess


# 创建一个新的 Popen 类，并继承自 subprocess.Popen
class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        # 在调用父类（即 subprocess.Popen）的构造方法时，将 encoding 参数直接置为 UTF-8 编码格式
        super().__init__(encoding="UTF-8", *args, **kwargs)


# 必须要在导入 PyExecJS 模块前，就将 subprocess.Popen 类重置为新的类
subprocess.Popen = MySubprocessPopen
