from time import sleep

import utils.patch  # noqa: F401
from exceptions import handle_exception
from school import SchoolManager


@handle_exception
def main() -> None:
    """
    主函数
    """
    school = SchoolManager()
    # 登录
    school.login("2023533190", "Haoyu2548154697")
    print("登录成功...")
    sleep(1)
    # 获取课程信息
    print("获取课程信息...")
    school.get_lesson()
    print("获取课程信息成功...")


if __name__ == "__main__":
    main()
