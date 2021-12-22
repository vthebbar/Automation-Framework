import random
import string

class RandomEmail:

    @staticmethod
    def random_email(n):
        choices = string.ascii_lowercase + "0123456789."
        email_id = random.choice(string.ascii_lowercase)
        for x in range(n-1):
            email_id = email_id + random.choice(choices)
        email_id = email_id + "@gmail.com"
        return email_id


# Below code is to test the above function
    email = random_email(8)
    print(email)