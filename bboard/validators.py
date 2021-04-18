from django.core.exceptions import ValidationError


def min_5_chars(string):
    if len(string) < 5:
        raise ValidationError('Должно быть минимум 5 символов')


def not_number_validator():
    pass


class NotNumberValidator:
    def __call__(self):
        pass
