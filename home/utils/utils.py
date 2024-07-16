

def is_administrador(user):
    return user.is_authenticated and user.tipo == 'administrador'