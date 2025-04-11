from social_core.exceptions import AuthAlreadyAssociated

def prevent_duplicate_social_login(strategy, backend, uid, user=None, *args, **kwargs):
    social = backend.strategy.storage.user.get_social_auth(backend.name, uid)
    if social and user and social.user != user:
        # You can either raise or redirect:
        # raise AuthAlreadyAssociated(backend, 'This account is already in use.')
        return strategy.redirect('/auth-error/')  # safer for user
