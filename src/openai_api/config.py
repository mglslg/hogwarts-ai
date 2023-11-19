__assistant_config = [{
    "name": "Dobby",
    "id": "asst_HhXfMHbakJFuPB7SSSsaWEvG"
}, {
    "name": "Math Tutor",
    "id": "asst_HhXfMHbakJFuPB7SSSsaWEvG"
}]


def get_assistant_by_name(name):
    for assistant in __assistant_config:
        if assistant['name'] == name:
            return assistant['id']
    return None
