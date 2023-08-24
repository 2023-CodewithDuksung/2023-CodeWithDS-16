from django import forms
from django.contrib.auth.forms import AuthenticationForm

class DuksungEmailAuthenticationForm(AuthenticationForm):
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': "제공된 계정 정보가 올바르지 않습니다. 학교 계정을 확인해 주세요.",
    }

    def confirm_login_allowed(self, user):
        if not user.email.endswith('@duksung.ac.kr'):
            raise forms.ValidationError("등록된 학교 이메일 계정이 아닙니다. 이메일 형식을 확인해 주세요.")
        super().confirm_login_allowed(user)
