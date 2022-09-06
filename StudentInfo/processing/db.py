import json


class MysqlDatabases:
    def __init__(self):
        self.users = json.loads(open('./admin.json', mode='r', encoding='utf-8').read())
        self.students = json.loads(open('./Students_Info_DB.json', mode='r', encoding='utf-8').read())

    def check_login(self, username, password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登录成功'
                else:
                    return False, '登录失败，密码错误'
            return False, '登录失败，用户名不存在'
        return self.users

    def all(self):
        return self.students

    def insert(self, student):
        self.students.append(student)

    def delete_by_number(self, num):
        for student in self.students:
            if student['stu_num'] == num:
                self.students.remove(student)
                return True, f'学号为 {num} 的学生数据删除成功'
        return False, f'学号为 {num} 的学生不存在数据库中'

    def search_by_number(self, num):
        print(num)
        for student in self.students:
            if student['stu_num'] == num:
                return True, student
            else:
                return False, f'学号为 {num} 的学生不存在数据库中'

    # def update(self, num):
    #     for student in self.students:
    #         if student['stu_num'] == num['stu_num']:
    #             num.update(num)
    #             return True, f'学号为 {num["name"]} 的学生数据修改成功'
    #     return False, f'学号为 {num["name"]} 的学生不存在数据库中'


db = MysqlDatabases()

if __name__ == '__main__':
    print(db.check_login('admin', 'Skills39'))
    print(db.all())
