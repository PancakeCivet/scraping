from pydantic import BaseModel, Field


class LoginForm(BaseModel):
    """
    登录表单
    """

    username: str
    password: str
    execution: str
    captcha: str = ""
    eventId: str = Field(default="submit", alias="_eventId")
    cllt: str = "userNameLogin"
    dllt: str = "generalLogin"
    lt: str = ""


class LessonForm(BaseModel):
    """
    选课表单
    """

    lesson_id: int
    """课程id"""
    lesson_operate: bool
    """是否选课"""

    def to_dict(self) -> dict[str, str]:
        optype = "true" if self.lesson_operate else "false"
        lesson_operate = "true" if self.lesson_operate else "false"
        if self.lesson_operate:
            operator0 = f"{self.lesson_id}:{lesson_operate}:0"
        else:
            operator0 = f"{self.lesson_id}:{lesson_operate}"
        return {
            "optype": optype,
            "operator0": operator0,
        }


class Cookies(BaseModel):
    """
    Cookies
    """

    JSESSIONID: str
    srv_id: str

    def to_record(self) -> dict[str, str]:
        return {"Cookie": f"JSESSIONID={self.JSESSIONID}; srv_id={self.srv_id}"}


class ArrangeInfo(BaseModel):
    """
    排课信息
    """

    weekDay: int
    """星期几"""
    weekState: str
    """周状态"""
    startUnit: int
    """开始节"""
    endUnit: int
    """结束节"""
    weekStateDigest: str
    """周状态摘要"""
    startTime: int
    """开始时间"""
    endTime: int
    """结束时间"""
    roomIds: str
    """教室id"""
    rooms: str
    """教室"""


class Lesson(BaseModel):
    """
    课程类
    """

    id: int
    """id"""
    no: str
    """课程序号"""
    name: str
    """课程名称"""
    code: str
    """课程代码"""
    credits: float
    """学分"""
    courseId: int
    """课程id"""
    startWeek: int
    """开始周"""
    endWeek: int
    """结束周"""
    courseTypeId: int
    """课程类型id"""
    courseTypeName: str
    """课程类型名称"""
    courseTypeCode: str
    """课程类型代码"""
    teachDepartId: int
    """教学部id"""
    teachDepartName: str
    """教学部名称"""
    scheduled: bool
    """是否已排课"""
    hasTextBook: bool
    """是否有教材"""
    period: int
    """总课时"""
    weekHour: int
    """周课时"""
    withdrawable: bool
    """可退课"""
    textbooks: str
    """教材"""
    teachers: str
    """教师"""
    teacherIds: str
    """教师id"""
    campusCode: str
    """校区代码"""
    campusName: str
    """校区名称"""
    courseEducationId: str
    """课程教育id"""
    courseEducationName: str
    """课程教育名称"""
    strMainTeacherId: str
    """主教师id"""
    strSemester: str
    """学期"""
    remark: str
    """备注"""
    teachClassName: str
    """教学班名称"""
    preRequirement: str
    """先修课程"""
    similarcourses: str
    """相似课程"""
    byThrough: str
    """是否通过"""
    bstdLimit: str
    """本科生限制"""
    bstdCount: str
    """本科生人数"""
    ystdLimit: str
    """研究生限制"""
    ystdCount: str
    """研究生人数"""
    arrangeInfo: list[ArrangeInfo]
    """排课信息"""
