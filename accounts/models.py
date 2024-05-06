from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email,first_name,last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
      
        user.set_password(password)
        user.save()

        return user
    







class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    cedula = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_rectora = models.BooleanField(default=False)
    is_investigacion = models.BooleanField(default=False)
    is_vinculacion = models.BooleanField(default=False)
    is_coor_academica = models.BooleanField(default=False)
    is_coor_estrategico = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)
    is_estudiante = models.BooleanField(default=False)
    is_administrativo1 = models.BooleanField(default=False)
    is_administrativo2 = models.BooleanField(default=False)
    is_administrativo3 = models.BooleanField(default=False) # Sirva para habilitar el registro de documentos de acreditacion
    is_visitante = models.BooleanField(default=False)
    is_adminBolsa = models.BooleanField(default=False) # Sirva para habilitar el registro de documentos de acreditacion
    is_adminBiblioteca = models.BooleanField(default=False)
    is_adminInventario = models.BooleanField(default=False)
    
    

    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name) 

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email