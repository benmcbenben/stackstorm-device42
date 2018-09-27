from lib.base_action import BaseAction


class CreateBuilding(BaseAction):
    def run(self, name, address=None, contact_name=None, contact_phone=None, tags=None,
            rooms=None):

        payload = {'name': name}
        if address:
            payload['address'] = address
        if contact_name:
            payload['contact_name'] = contact_name
        if contact_phone:
            payload['contact_phone'] = contact_phone
        if tags:
            payload['tags'] = tags

        print("payload: %s" % payload)
        d42_headers = {'Accept': 'application/json'}
        response = self.post(
            endpoint="buildings/",
            payload=payload,
            headers=d42_headers
        )
        # d42 api agent returns response.json(0) if response.ok...:
        if type(response) is dict:
            return response
        else:
            return response.text
