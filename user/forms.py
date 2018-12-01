# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 0028 16:04
# @Author  : zhyipeng
# @File    : forms.py

from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    '''
    个人资料表单
    '''
    class Meta:
        model = Profile
        fields = [
            'id',
            'location',
            'min_distance',
            'max_distance',
            'min_dating_age',
            'max_dating_age',
            'dating_sex',
            'vibration',
            'only_matche',
            'auto_play',
        ]

    def clean_max_dating_age(self):
        '''
        数据清洗
        :return:
        '''
        cleaned_data = super().clean()
        print(cleaned_data)
        min_dating_age = cleaned_data.get('min_dating_age')
        max_dating_age = cleaned_data.get('max_dating_age')
        if min_dating_age > max_dating_age:
            raise forms.ValidationError
        return max_dating_age


# class UploadForm(forms.Form):
#     '''
#     文件上传表单
#     '''
#     avatar = forms.ImageField()