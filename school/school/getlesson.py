import execjs
from requests import Session

from exceptions import SchoolException

from .const import LESSION_HEADERS
from .typing import Lesson


class GetLessonHandler:
    """
    获取课程信息
    """

    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session
        self.session.headers.clear()
        self.session.headers.update(LESSION_HEADERS)

    def init(self) -> None:
        url = "https://eams.shanghaitech.edu.cn/eams/stdElectCourse!innerIndex.action"
        response = self.session.get(url)
        if response.status_code != 200:
            raise SchoolException("初始化失败")

    def get_lession_info(self) -> str:
        """
        获取课程信息
        """
        url = "https://eams.shanghaitech.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=2345"
        cookie = self.session.cookies.get_dict()
        jasessionid = cookie.get("JSESSIONID")
        srv_id = cookie.get("srv_id")
        cookie = {"JSESSIONID": jasessionid, "srv_id": srv_id}
        self.session.cookies.clear()
        self.session.cookies.update(cookie)
        response = self.session.get(url)
        if response.status_code != 200:
            raise SchoolException("获取课程信息失败")

        url = "https://eams.shanghaitech.edu.cn/eams/stdElectCourse!data.action?profileId=2345"
        response = self.session.get(url)
        if response.status_code != 200:
            raise SchoolException("获取课程信息失败")
        return response.text

    def get_lession_info_obj(self, js_str: str) -> list[Lesson]:
        """
        获取课程信息
        """
        ctx = execjs.compile(js_str)
        data = ctx.eval("lessonJSONs")
        return [Lesson.model_validate(item) for item in data]
