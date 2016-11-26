import re

emoji_re = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags=re.UNICODE)


def reply_from(iid, msg):
    if is_reply(msg):
        if msg['reply_to_message']['from']['id'] == iid:
            return True
    return False


def msg_contains(msg, substr):
    contains = False
    if 'text' in msg:
        contains = msg['text'].find(substr) > -1
    if 'caption' in msg:
        contains = msg['caption'].find(substr) > -1

    return contains

def is_reply(msg):
    if 'reply_to_message' in msg:
        return True
    return False

def is_self_reply(msg):
    if is_reply(msg):
        reply = msg['reply_to_message']
        if reply['from']['id'] == msg['from']['id']:
            return True
    return False


class AchievementBase:
    name = None
    levels = []

    def update(self, msg, content_type, achievements_counters):
        return achievements_counters

    # global_counters = {
    # 'forward_from_channel': int,
    # 'text': int,
    # 'game': int,
    # 'voice': int,
    # 'sticker': int,
    # 'document': int,
    # 'photo': int,
    # 'reply_to_message': int,
    # 'sum_message_length': int,
    # 'location': int,
    # 'messages': int,
    # 'video': int,
    # 'audio': int,
    # 'last_message_date': timestamp,
    # 'last_left_chat': timestamp,
    # 'forward': int,
    # 'average_msg_length': int
    # }
    # achievement_counters = any dict

    def check(self, msg, content_type, counters):
        return False

    def get_level(self, count):
        if count == 0:
            return 0

        if len(self.levels) > 0:
            for i in range(0, len(self.levels)):
                if count < self.levels[i]:
                    return i
            return i + 1
        else:
            return 0


class FirstMessage(AchievementBase):
    name = 'Добро пожаловать'
    levels = [1, 5, 10]

    def check(self, msg, content_type, counters):
        return content_type == 'text'


class StickerSpammer(AchievementBase):
    name = 'sticker spammer'
    levels = [2, 5, 10]

    def check(self, msg, content_type, counters):
        return content_type == 'sticker'


class SantaShpaker(AchievementBase):
    name = 'Santa Shpaker'
    levels = [2, 5, 10]

    def check(self, msg, content_type, counters):
        # it's shpaker id
        return reply_from(9429534, msg)


class BackTo2007(AchievementBase):
    name = 'Назад в 2007'
    levels = [2, 5, 10]

    def check(self, msg, content_type, counters):
        if 'text' in msg:
            count = 0
            for emoji in emoji_re.finditer(msg['text']):
                s, e = emoji.span()
                count += e - s
            return count >= 5


class WhyDoYouAsk(AchievementBase):
    name = 'А ви таки зачем интересуетесь?'
    levels = [1, 2, 3]

    def check(self, msg, content_type, counters):
        count = 0
        if is_reply(msg) and content_type == 'text':
            reply = msg['reply_to_message']
            if not is_self_reply(msg) and 'text' in reply:
                _len = len(msg['text']) > 4 and len(reply['text']) > 4
                return reply['text'][-1] == '?' and msg['text'][-1] == '?' and _len


class Dzhugashvili(AchievementBase):
    name = 'Джугашвили'
    levels = [1]

    def update(self, msg, content_type, achievements_counters):
        if achievements_counters is None:
            achievements_counters = {
                'links_in_row': 0
            }
        if content_type == 'text':
            links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                               msg['text'])
            entities_link = None
            if 'entities' in msg:
                for entitie in msg['entities']:
                    entities_link = entitie['type'] == 'text_link'

            if len(links) > 0 or entities_link is not None:
                achievements_counters['links_in_row'] += 1
            else:
                achievements_counters['links_in_row'] = 0
        else:
            achievements_counters['links_in_row'] = 0

        return achievements_counters

    def check(self, msg, content_type, counters):
        return counters['local']['links_in_row'] >= 3



registered_achievements = [
    FirstMessage,
    StickerSpammer,
    SantaShpaker,
    BackTo2007,
    WhyDoYouAsk,
    Dzhugashvili
]

__all__ = ['registered_achievements']
