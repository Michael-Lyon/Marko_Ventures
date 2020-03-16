from django.test import TestCase, Client
from django.urls import reverse
from core.forms import CreationUserForm as Form


class TestForms(TestCase):
    # Testing the Labels
    def test_username_label(self):
        form = Form()
        usernameLabel = form.fields['username'].label
        self.assertTrue(usernameLabel == None or usernameLabel == 'username')

    def test_email_label(self):
        form = Form()
        emailLabel = form.fields['email'].label
        self.assertTrue(emailLabel == None or emailLabel == 'email')

    def test_password1_label(self):
        form = Form()
        passwordLabel1 = form.fields['password1'].label
        self.assertTrue(passwordLabel1 ==
                        None or passwordLabel1 == 'password1')

    def test_password2_label(self):
        form = Form()
        passwordLabel2 = form.fields['username'].label
        self.assertTrue(passwordLabel2 ==
                        None or passwordLabel2 == 'password2')

    def test_form_IsCorrect(self):
        form = Form(data={
            'username': 'mike',
            'email': 'mike@mike.com',
            'password1': 'chinonsoisachinonso12',
            'password2': 'chinonsoisachinonso12'
        })
        self.assertTrue(form.is_valid())

    def test_form_IsNot_valid(self):
        form1 = Form(data={
            'username': '',
            'email': 'mikem',
            'password1': 'choionso12',
            'password2': 'chinonsoionhcj3332'})

        self.assertEquals(len(form1.errors), 3)
        self.assertFalse(form1.is_valid())
