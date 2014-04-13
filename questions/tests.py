# coding: utf-8
import re
from django.core import mail
# from django_webtest import WebTest
# from django.test import TestCase

class AuthTest(WebTest):
    fixtures = ['users.json']

    def testLogoutAndLogin(self):
        page = self.app.get('/', user='kmike')
        page = page.click(u'Выйти').follow()
        assert u'Выйти' not in page
        login_form = page.click(u'Войти', index= 0).form
        login_form['email'] = 'example@example.com'
        login_form['password'] = '123'
        result_page = login_form.submit().follow()
        assert u'Войти' not in result_page
        assert u'Выйти' in result_page

    def testEmailRegister(self):
        register_form = self.app.get('/').click(u'Регистрация').form
        self.assertEqual(len(mail.outbox),  0)
        register_form['email'] = 'example2@example.com'
        register_form['password'] = '123'
        assert u'Регистрация завершена' in register_form.submit().follow()
        self.assertEqual(len(mail.outbox), 1)

        # активируем аккаунт и проверяем, что после активации
        # пользователь сразу видит свои покупки
        mail_body = unicode(mail.outbox[ 0].body)
        activate_link = re.search('(/activate/.*/)', mail_body).group(1)
        activated_page = self.app.get(activate_link).follow()
        assert u'<h1>Вопросы пользователей</h1>' in activated_page
# Create your tests here.
