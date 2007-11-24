from django.conf import settings
from django.db.models import get_model

from django.contrib.auth.models import SiteProfileNotAvailable


def get_profile_model():
    """
    Returns the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting.
    
    """
    if not settings.AUTH_PROFILE_MODULE:
        raise SiteProfileNotAvailable
    profile_mod = get_model(*settings.AUTH_PROFILE_MODULE.split('.'))
    if not profile_mod:
        raise SiteProfileNotAvailable
    return profile_mod
