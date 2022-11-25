from django.conf import settings
from django.db.models import Max
from user import models


def create_userid_num():
    max_id = models.Users.objects.aggregate(Max('id')).get("id__max")  # 获取最新创建的那个用户的自增ID
    new_id_num = settings.INVALID_USER_NUMBER

    if max_id is None:
        # 数据库没有用户，用户id从1000开始，最初的用户ID：Tomboy_1000
        new_id_num = settings.MIN_USER_NUMBER
    else:
        try:
            # 判断Tomboy_8023用户是不是第一位用户，如果是，则userid序号从最小序号1000开始
            user = models.Users.objects.filter(id=max_id).values("userid").first()
            max_userid = user.get('userid')
            old_id_num = int(max_userid.split('_')[1])
            if old_id_num == settings.OWNER_USER_NUMBER:
                first_user = models.Users.objects.filter(id=1)
                if first_user and max_id == 1:
                    new_id_num = settings.MIN_USER_NUMBER
                else:
                    # Tomboy_8023用户不是第一位用户，取Tomboy_8023前面的一位用户的userid序号并+1形成新的userid序号
                    # 如果新的userid序号 == 8023 则令新的userid序号为8024
                    old_user = models.Users.objects.filter(id=max_id - 1)
                    new_id_num = int(old_user[0].userid.split('_')[1]) + 1
                    if new_id_num == 8023:
                        new_id_num += 1
            else:
                new_id_num = old_id_num + 1
                if new_id_num == settings.OWNER_USER_NUMBER:
                    new_id_num += 1
        except AttributeError as e:
            print(e)
            # 增加日志模块

    return new_id_num


def create_userid():
    new_userid = settings.USERID_STARTSWITH
    new_id_num = create_userid_num()

    new_userid += str(new_id_num)
    print(new_userid)
    return new_userid
