class ValidPassword:
    """
    功能：檢查密碼是否符合規則
    維護：若有不同的字串檢測需求，直接繼承並改寫 __init__ 的self.default即可
    """

    is_instance = None

    def __call__(self, pw):
        """
        入口
        1._check: 檢查密碼格式 -> str or not null
        2._scan: 掃描密碼 -> 密碼是否符合規定字符
        """
        return self._check(pw)._scan(pw)

    def __init__(self):
        """
        s.digits: [0-9]
        s.ascii_letters: [a-zA-Z]
        s.punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        """
        s = __import__("string")
        SPACE = ' '
        self.default = s.digits + s.ascii_letters + s.punctuation + SPACE

    @classmethod
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls) if cls.is_instance is None else cls.is_instance

    def __repr__(self):
        return f"如果密碼不在規定字串內就報錯，字串如下:\n{self.default}"

    def _check(self, pw):
        if not pw:
            raise ValueError(error_code=_.PW_FORMAT_INVALID)
        if not isinstance(pw, str):
            raise TypeError("== Password must be String ==")
        return self

    def _scan(self, pw):
        for txt in pw:
            if not self._pw_map(get=txt):
                raise ValueError("== Invalid password ==")
        return pw

    def _pw_map(self, get):
        return {txt: 1 for txt in self.default}.get(get)


pwValid = ValidPassword()
