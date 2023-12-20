import itertools as its
import datetime

# 记录程序运行时间
start = datetime.datetime.now()

# 定义密码字符集合
character_set = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'  # 大小写字母 + 数字 组合
# character_set = '0123456789'  # 纯数字

# 生成密码的位数
password_length = 8  # 即生成8位密码，正常情况下热点密码位数为8
password_combinations = its.product(character_set, repeat=password_length)

output_file_path = r"C:\Users\Administrator\Desktop\alphabetPass.txt"  # alphabetPass.txt 是密码本名称

with open(output_file_path, 'a') as password_file:
    for combination in password_combinations:
        password = ''.join(combination)
        password_file.write(password + '\n')
        print(password)

print('密码本生成好了')

end = datetime.datetime.now()
print("生成密码本一共用了多长时间：{}".format(end - start))

