
def user_directory_path(instance, filename):
    '''
    This functions helps save profile to a particular
    directory
    '''
    return f'user_{instance.user}/{filename}'
