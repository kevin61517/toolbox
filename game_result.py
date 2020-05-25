from datetime import datetime as t
# 頭銜(隊長/副隊長)
IS_CAPTAIN = 'captain'  # 總分 x 3
IS_VICE_CAPTAIN = 'vice_captain'  # 總分 x 1.5

# 身份
ID = 'id'

# 守備位置
FORWARD = 'forward'
MIDFIELDER = 'midfielder'
DEFENDER = 'defender'
GOALKEEPER = 'goalkeeper'

# 比賽數值、行為
MINUTE = 'minute'  # 上場時數
GOAL = 'goal'  # 進球
ASSIST = 'assist'  # 助攻
PASS = 'pass'  # 傳球
SHOOT = 'shoot'  # 射門
CLEAN_SHEET = 'clean_sheet'  # 完封
SHOT_SAVE = 'shot_save'  # 防止射門
PENALTY_SAVE = 'penalty_save'  # 防止罰球
SUCCESSFUL_TACKLES_MADE = 'successful_tackles_made'  # 鏟球
RED = 'red'  # 紅牌
YELLOW = 'yellow'  # 黃牌
OWN_GOAL = 'own_goal'  # 烏龍球
BE_GOAL = 'be_goal'  # 失分(被進球)
PENALTY_FAIL = 'penalty_fail'  # 罰球失敗

# 計算規則
# normal
CAL_ASSIST = 5
CAL_PASS = (5/100)
CAL_SHOOT = (1/2)
CAL_SUCCESSFUL_TACKLES_MADE = 1
CAL_YELLOW = -1
CAL_RED = -3
CAL_OWN_GOAL = -2
CAL_PENALTY_FAIL = -2

# forward
FORWARD_GOAL = 8

# midfielder
MIDFIELDER_GOAL = 9
MIDFIELDER_CLEAN_SHEET = 1

# defender
DEFENDER_GOAL = 10
DEFENDER_CLEAN_SHEET = 5
DEFENDER_BE_GOAL = -(1/2)

# goalkeeper
GOALKEEPER_GOAL = 10
GOALKEEPER_CLEAN_SHEET = 5
GOALKEEPER_SHOT_SAVE = 2
GOALKEEPER_PENALTY_SAVE = 9
GOALKEEPER_BE_GOAL = -(1/2)

# 計算規則
CAPTAIN = 3
VICE_CAPTAIN = 1.5

forward = {
    ID: 13,
    FORWARD: 1,
    MIDFIELDER: 0,
    DEFENDER: 0,
    GOALKEEPER: 0,
    MINUTE: 87,
    GOAL: 1,
    ASSIST: 15,
    PASS: 23,
    SHOOT: 19,
    CLEAN_SHEET: 3,
    SHOT_SAVE: 5,
    PENALTY_SAVE: 5,
    SUCCESSFUL_TACKLES_MADE: 6,
    RED: 0,
    YELLOW: 2,
    OWN_GOAL: 0,
    BE_GOAL: 0,
    PENALTY_FAIL: 3
}

midfielder = {
    ID: 87,
    FORWARD: 0,
    MIDFIELDER: 1,
    DEFENDER: 0,
    GOALKEEPER: 0,
    MINUTE: 87,
    GOAL: 1,
    ASSIST: 15,
    PASS: 23,
    SHOOT: 19,
    CLEAN_SHEET: 3,
    SHOT_SAVE: 5,
    PENALTY_SAVE: 5,
    SUCCESSFUL_TACKLES_MADE: 6,
    RED: 0,
    YELLOW: 2,
    OWN_GOAL: 0,
    BE_GOAL: 0,
    PENALTY_FAIL: 3
}

defender = {
    ID: 2,
    FORWARD: 0,
    MIDFIELDER: 0,
    DEFENDER: 1,
    GOALKEEPER: 0,
    MINUTE: 87,
    GOAL: 1,
    ASSIST: 15,
    PASS: 23,
    SHOOT: 19,
    CLEAN_SHEET: 3,
    SHOT_SAVE: 5,
    PENALTY_SAVE: 5,
    SUCCESSFUL_TACKLES_MADE: 6,
    RED: 0,
    YELLOW: 2,
    OWN_GOAL: 0,
    BE_GOAL: 0,
    PENALTY_FAIL: 3
}

goalkeeper = {
    ID: 42,
    FORWARD: 0,
    MIDFIELDER: 0,
    DEFENDER: 0,
    GOALKEEPER: 1,
    MINUTE: 87,
    GOAL: 1,
    ASSIST: 15,
    PASS: 23,
    SHOOT: 19,
    CLEAN_SHEET: 3,
    SHOT_SAVE: 5,
    PENALTY_SAVE: 5,
    SUCCESSFUL_TACKLES_MADE: 6,
    RED: 0,
    YELLOW: 2,
    OWN_GOAL: 0,
    BE_GOAL: 0,
    PENALTY_FAIL: 3
}


class ScoreCalculator:
    def __init__(self, player_list):
        self.__player_list = player_list
        self.__player = None
        self.__result = list()
        self.__sum = 0

    def __normal_cal(self):
        self.__sum += self.__player[ASSIST] * CAL_ASSIST
        self.__sum += self.__player[PASS] * CAL_PASS
        self.__sum += self.__player[SHOOT] * CAL_SHOOT
        self.__sum += self.__player[SUCCESSFUL_TACKLES_MADE] * CAL_SUCCESSFUL_TACKLES_MADE
        self.__sum += self.__player[YELLOW] * CAL_YELLOW
        self.__sum += self.__player[RED] * CAL_RED
        self.__sum += self.__player[OWN_GOAL] * CAL_OWN_GOAL
        self.__sum += self.__player[PENALTY_FAIL] * CAL_PENALTY_FAIL

    def __forward(self):
        self.__sum += self.__player[GOAL] * FORWARD_GOAL

    def __midfielder(self):
        self.__sum += self.__player[GOAL] * MIDFIELDER_GOAL
        self.__sum += self.__player[CLEAN_SHEET] * MIDFIELDER_CLEAN_SHEET

    def __defender(self):
        self.__sum += self.__player[GOAL] * DEFENDER_GOAL
        self.__sum += self.__player[CLEAN_SHEET] * DEFENDER_CLEAN_SHEET
        self.__sum += self.__player[BE_GOAL] * DEFENDER_BE_GOAL

    def __goalkeeper(self):
        self.__sum += self.__player[GOAL] * GOALKEEPER_GOAL
        self.__sum += self.__player[CLEAN_SHEET] * GOALKEEPER_CLEAN_SHEET
        self.__sum += (self.__player[SHOT_SAVE] // 3) * GOALKEEPER_SHOT_SAVE
        self.__sum += self.__player[PENALTY_SAVE] * GOALKEEPER_PENALTY_SAVE
        self.__sum += self.__player[BE_GOAL] * GOALKEEPER_BE_GOAL

    def do(self):
        for self.__player in self.__player_list:
            _dict = dict()
            self.__normal_cal()
            if self.__player[FORWARD]:
                self.__forward()

            if self.__player[MIDFIELDER]:
                self.__midfielder()

            if self.__player[DEFENDER]:
                self.__defender()

            if self.__player[GOAL]:
                self.__goalkeeper()

            _dict[ID] = self.__player[ID]
            _dict['score'] = self.__sum
            self.__result.append(_dict)
            self.__sum = 0

        return self.__result
