from lxml import etree
from requests import Session

from exceptions import SchoolException

from .const import LOGIN_HEADERS
from .typing import LoginForm

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}


class LoginHandler:
    """
    登录处理器
    """

    session: Session

    def __init__(self, seesion: Session) -> None:
        self.session = seesion
        self.session.headers.clear()
        self.session.headers.update(headers)

    def get_login_html(self) -> str:
        """
        获取url的内容
        """
        url = "https://ids.shanghaitech.edu.cn/authserver/login"
        response = self.session.get(url)
        if response.status_code != 200:
            raise SchoolException("获取登录页面失败")
        return response.text

    def get_info(self, html: str) -> tuple[str, str]:
        """
        获取信息
        """
        root = etree.HTML(html, None)
        pwdEncryptSalt = root.xpath('//*[@id="pwdEncryptSalt"]')[0].attrib["value"]  # type: ignore
        excution = root.xpath('//*[@id="execution"]')[0].attrib["value"]  # type: ignore
        return excution, pwdEncryptSalt

    def do_login(self, data: LoginForm) -> None:
        """
        登录
        """

        url = "https://ids.shanghaitech.edu.cn/authserver/login"
        self.session.headers.clear()
        self.session.headers.update(LOGIN_HEADERS)
        self.session.cookies.update(
            {
                "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "zh_CN"
            }
        )
        response = self.session.post(
            url, data=data.model_dump(by_alias=True), allow_redirects=True
        )
        if response.status_code != 200:
            raise SchoolException("登录失败")
