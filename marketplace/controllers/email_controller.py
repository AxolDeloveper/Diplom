import hashlib
import random
import smtplib
from email.mime.text import MIMEText


class EmailControlles:
    def __init__(self, taker, message, subject):
        self._codess = self.__generate_code(8)
        self.code = self.__hash_code(str(self._codess))

        self.__email = 'fdfgfdggfd@list.ru'
        self.__password = 'i7Dayqy9Be3YywkeEX1L'

        self.code_message = str(message + ' ' + self._codess)
        self.subject = subject
        self.taker = taker
        self.codessss = self._codess

    def __generate_code(self, lenght: int):
        nums = '0123456789'
        words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        special_symbols = '_*()$@'

        super_str = ''.join(nums + words + special_symbols)

        res = []
        for key in range(lenght):
            res.append(
                random.choice(super_str)
            )

        return ''.join(res)


    def send_code(self):
        sender = self.__email
        password = self.__password


        server = smtplib.SMTP("smtp.mail.ru", 587)
        server.starttls()

        server.login(sender, password)
        msg = MIMEText(self.code_message)
        msg["Subject"] = self.subject
        server.sendmail(sender, str(self.taker), msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return self.__hash_code(str(self._codess))

    def send_message(self, message):
        sender = self.__email
        password = self.__password

        server = smtplib.SMTP("smtp.mail.ru", 587)
        server.starttls()

        server.login(sender, password)
        msg = MIMEText(str(message))
        msg["Subject"] = self.subject
        server.sendmail(sender, str(self.taker), msg.as_string())

        return self.__hash_code(str(self._codess))

    def __hash_code(self, code: str):
        return hashlib.sha256(code.encode()).hexdigest()



    def test(self):
        tests = self.__generate_code(8)
        print(tests)
        print(tests)