from time import sleep

from requests import Session

from utils.encrypt import get_encrypt_str

from .getlesson import GetLessonHandler
from .login import LoginHandler
from .operater import Operater
from .typing import Lesson, LoginForm


class SchoolManager:
    """
    学校处理器
    """

    session: Session
    lessons: list[Lesson]

    def __init__(self) -> None:
        self.session = Session()

    def login(self, username: str, password: str) -> None:
        """
        登录
        """

        handler = LoginHandler(self.session)
        html = handler.get_login_html()
        execution, pwdEncryptSalt = handler.get_info(html)
        password = get_encrypt_str(password, pwdEncryptSalt)
        data = LoginForm(username=username, password=password, execution=execution)
        handler.do_login(data)

    def get_lesson(self) -> None:
        """
        获取课程信息
        """

        handler = GetLessonHandler(self.session)
        handler.init()
        sleep(1)
        lesson = handler.get_lession_info()
        self.lessons = handler.get_lession_info_obj(lesson)
        print(self.lessons)

    def choose_lesson(self, id: int, Choose: bool) -> bool:
        """
        选课
        """

        handler = Operater(self.session)
        return handler.operate_lesson(id, Choose)
