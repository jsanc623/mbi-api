from mbi_validation import is_alpha, is_numeric, is_alphanumeric
import string
import random


class MBI:
    def __init__(self, mbi: str):
        mbi = "" if mbi is None else mbi

        # assign mbi to self.mbi,
        self.mbi = ''.join([i.replace('-', '') for i in mbi]).strip().lower()
        pass

    def validate(self):
        errors = []
        if len(self.mbi) != 11:
            errors.append("length requirement failure, length: " + str(len(self.mbi)))
            return len(errors) == 0, errors

        if not is_numeric(self.mbi[0], False):
            errors.append("expected numeric value, position 1")

        for idx in [2, 5, 8, 9]:
            if not is_alpha(self.mbi[idx - 1]):
                errors.append("expected alphabetic value, position " + str(idx))

        for idx in [3, 6]:
            if not is_alphanumeric(self.mbi[idx - 1]):
                errors.append("expected alphanumeric value, position " + str(idx))

        for idx in [4, 7, 10, 11]:
            if not is_numeric(self.mbi[idx - 1]):
                errors.append("expected numeric value, position " + str(idx))

        return len(errors) == 0, errors

    @staticmethod
    def generate():
        acceptable_letters = 'acdefghjkmnpqrtuvwxy'

        def alpha():
            return random.choice(acceptable_letters)

        def numeric(start=0):
            return random.choice(string.digits[start:9])

        def alphanumeric():
            return random.choice(string.digits + acceptable_letters)

        generated_mbi = list()
        generated_mbi.append(numeric(1))  # 1
        generated_mbi.append(alpha())  # 2
        generated_mbi.append(alphanumeric())  # 3
        generated_mbi.append(numeric())  # 4
        generated_mbi.append(alpha())  # 5
        generated_mbi.append(alphanumeric())  # 6
        generated_mbi.append(numeric())  # 7
        generated_mbi.append(alpha())  # 8
        generated_mbi.append(alpha())  # 9
        generated_mbi.append(numeric())  # 10
        generated_mbi.append(numeric())  # 11

        return "".join(generated_mbi)
