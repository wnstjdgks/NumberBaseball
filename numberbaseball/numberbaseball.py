import random
import copy
import sys
from typing import List
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from numberbaseball.ui.baseball_ui import Ui_NumberBaseball


class UserInput:
    def __init__(self, user_input: List[int]):
        self._user_input = user_input

    @classmethod
    def create(cls, input_numbers: str):
        cls.validate(input_numbers)
        return cls([int(x) for x in input_numbers])

    @classmethod
    def validate(cls, user_input: str):
        if len(user_input) != 3:
            raise ValueError("The input must consist of exactly three digits.")

        if not user_input.isdigit():
            raise ValueError("All inputs must be digits (0-9).")

        if len(set(user_input)) != 3:
            raise ValueError("All inputs must not be duplicated.")

    def get_user_input(self):
        return copy.copy(self._user_input)


class NumberBaseball:
    MIN_NUMBER = 0
    MAX_NUMBER = 10
    ANSWER_STRIKE_COUNT = 3
    ANSWERS_COUNT = 3

    def __init__(self, answers: List[int]):
        self.validate(answers)
        self.answers = answers

    @classmethod
    def create(cls):
        numbers = random.sample(range(cls.MIN_NUMBER, cls.MAX_NUMBER), cls.ANSWERS_COUNT)
        return NumberBaseball(numbers)

    @classmethod
    def validate(cls, answers: List[int]):
        if len(answers) != cls.ANSWERS_COUNT:
            raise ValueError("The input must consist of exactly three digits.")

        # 올바른 범위 체크: 숫자가 MIN_NUMBER 이상이고 MAX_NUMBER 미만인지 확인
        if not all(cls.MIN_NUMBER <= x < cls.MAX_NUMBER for x in answers):
            raise ValueError(f"All inputs must be digits between {cls.MIN_NUMBER} and {cls.MAX_NUMBER - 1}.")

    def submit(self, user_input: 'UserInput'):
        strike, ball = self.calculate_result(user_input)

        if self.is_correct(strike):
            return "정답입니다."

        return f"볼 카운트 = {ball}, 스트라이크 카운트 = {strike}"

    def calculate_result(self, user_input: 'UserInput'):
        strike = 0
        ball = 0

        for i in range(3):
            current_user_number = user_input.get_user_input()[i]

            if current_user_number == self.answers[i]:
                strike += 1
            elif current_user_number in self.answers:
                ball += 1

        return strike, ball

    def is_correct(self, strike: int):
        return strike == self.ANSWER_STRIKE_COUNT

    def reset(self):
        self.answers = random.sample(range(self.MIN_NUMBER, self.MAX_NUMBER), self.ANSWERS_COUNT)


class BaseballApplication(QMainWindow, Ui_NumberBaseball):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.numberBaseball = NumberBaseball.create()
        self.lineEdit.setReadOnly(True)
        self.submitButton.clicked.connect(self.on_submit)
        self.resetButton.clicked.connect(self.on_reset)
        self.checkoutButton.clicked.connect(self.show_answer)

    def on_submit(self):
        try:
            user_input_str = self.InputTextEdit.text()
            user_input = UserInput.create(user_input_str)
            result = self.numberBaseball.submit(user_input)
            self.lineEdit.setText(result)

        except ValueError as e:
            QMessageBox.warning(self, "입력 오류", str(e))

    def on_reset(self):
        self.numberBaseball.reset()
        self.lineEdit.setText("게임이 리셋되었습니다.")
        self.InputTextEdit.clear()

    def show_answer(self):
        answer = "".join(map(str, self.numberBaseball.answers))
        self.lineEdit.setText(f"정답은 {answer}입니다.")


class Application:
    @staticmethod
    def run():
        app = QApplication(sys.argv)
        window = BaseballApplication()
        window.show()
        sys.exit(app.exec_())
