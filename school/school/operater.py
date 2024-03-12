from requests import Session

from .typing import LessonForm


class Operater:
    """
    操作类
    """

    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def operate_lesson(self, id: int, Choose: bool) -> bool:
        """
        根据id课程
        """

        url = "https://eams.shanghaitech.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=2345"
        form = LessonForm(lesson_id=id, lesson_operate=Choose)

        response = self.session.post(url, data=form.to_dict())
        if response.status_code != 200:
            return False
        return True
