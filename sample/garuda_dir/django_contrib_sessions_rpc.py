# DO NOT EDIT THIS FILE MANUALLY
# THIS FILE IS AUTO-GENERATED
# MANUAL CHANGES WILL BE DISCARDED
# PLEASE READ GARUDA DOCS
from garuda_dir.garuda_pb2 import Session, Void  # NOQA
from django.contrib.sessions.auto_crud import (  # NOQA
    read_session,
    delete_session,
    create_session,
    update_session,
    read_sessions_filter,
)


def session_to_dict(obj):
    # Cycle through fields directly
    d = {  }
    if obj is None:
        return d
    is_dj_obj = obj.__module__.endswith('models')
    foriegn_keys = []
    for field in ['expire_date', 'session_data', 'session_key']:  # NOQA
        value = getattr(obj, field, None)
        if field in [None, 'None']:
            continue
        d[field] = value
        if is_dj_obj and (field == 'id' or field in foriegn_keys):
            d[field] = str(value)
        elif is_dj_obj and field in ['created_on', 'updated_on']:
            d[field] = value.isoformat()
    return d


class SessionGaruda:

    def ReadSessionsFilter(self, void, context):
        objs = read_sessions_filter()
        return [Session(
            **session_to_dict(obj)) for obj in objs]

    def ReadSession(self, id, context):
        obj = read_session(id=id.id)
        return Session(**session_to_dict(obj))

    def CreateSession(self, obj, context):
        obj = create_session(**session_to_dict(obj))
        return Session(**session_to_dict(obj))

    def UpdateSession(self, obj, context):
        obj_dict = session_to_dict(obj)
        del obj_dict['id']
        obj = update_session(obj.id, **obj_dict)
        return Void()

    def DeleteSession(self, id, context):
        delete_session(id.id)
        return Void()