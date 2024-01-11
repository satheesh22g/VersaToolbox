def common_context(request):
    # Retrieve the username from the session or another source
    username = request.session.get('username', None)

    return {'username': username}