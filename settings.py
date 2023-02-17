user = {'name': 'Дмитрий', 'patronymic': 'Владимирович', 'last_name': 'Луконин'}

user_name_invalid_list = ['   ', '2', 'П', 'my name']
user_last_name_invalid_list = ['  ', '9', 'Ф', 'F', 'last name']

email_valid = '*********'
email_empty = ''
email_invalid_list = ['майл.ru', '@', '4@ru', 'test', '@test.com']


password_valid = '*********'
password_empty = ''
password_invalid_list = ['aad7dads', 'terkakfja', '4m', 'test', '01', '!!!ВотТакойЯхочуПроверитьПароль!!!', 'парол123',
                         'Fgdt6yuKFG']


phone_number_valid = '**************'
phone_number_empty = ''
phone_number_invalid_list = ['+35198', 353, 922255858, '-1-5-8', '922-355-']

login_valid = '*******************'
login_empty = ''
login_invalid_list = ['Login', '353', '*7^%$#@()', 'l', 'логин']


ls_valid = '123456789951'
ls_empty = ''
ls_invalid_list = ['счет', '353', '*7^%$#@()', 'g', 'EKLMN8721984476592876475978145987149787']


base_url = 'https://b2c.passport.rt.ru/'
recovery_url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?"

