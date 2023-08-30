def get_context(request):
    print("This function triggered")
    return {
        "title": "About",
    }