class RewardToWinner2:
    @classmethod
    def __package(cls, contest_result, rank, **key):
        for index in range(rank - 1, len(contest_result)):
            if contest_result[index]['rank'] == rank:
                contest_result[index]['prize_id'] = key.get('prize_id')
                contest_result[index]['prize'] = key.get('prize')
                contest_result[index]['modify_prize'] = key.get('modify_prize', 0)

            else:
                break
        return contest_result

    @classmethod
    def __get_rank_list(cls, contest_result):
        return [result['rank'] for result in contest_result]

    @classmethod
    def __format_data_to_set_list(cls, _list):
        return list(set(_list))

    @classmethod
    def __match_reward_rank_add_log(cls, _set, _list, contest_result, reward_map):
        for rank in _set:
            nums = _list.count(rank)
            if nums > 1:
                temp = rank
                money = 0
                for i in range(nums):
                    if reward_map.get(temp):
                        money += reward_map.get(temp)['prize']
                        temp += 1

                _id = reward_map.get(rank)['id']
                prize = reward_map.get(rank)['prize']
                modify_prize = money / nums
                cls.__package(contest_result, rank, prize=prize, prize_id=_id, modify_prize=modify_prize)

            else:
                if reward_map.get(rank):
                    prize = reward_map.get(rank)['prize']
                    _id = reward_map.get(rank)['id']
                    cls.__package(contest_result, rank, prize=prize, prize_id=_id)
                else:
                    break
        return contest_result

    @classmethod
    def do(cls, contest_result, reward_map):
        _list = cls.__get_rank_list(contest_result)
        _set = cls.__format_data_to_set_list(cls.__get_rank_list(contest_result))
        return cls.__match_reward_rank_add_log(_set, _list, contest_result, reward_map)