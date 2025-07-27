

def user_context(request):
    return {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else ''
    }
