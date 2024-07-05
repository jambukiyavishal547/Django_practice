from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser

class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **other_fields):
        if not phone:
            raise ValueError('Phone is required')
        other_fields['email'] = self.normalize_email(other_fields['email'])
        user = self.model(phone = phone, **other_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    def create_superuser(self, phone, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(phone, password, **other_fields)