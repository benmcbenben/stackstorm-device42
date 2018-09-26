from lib.base_action import BaseAction


class DeviceNameList(BaseAction):
    def run(self, last_updated_lt=None,
            last_updated_gt=None, first_added_lt=None, first_added_gt=None,
            custom_fields_and=None, custom_fields_or=None
            ):
        response = self.getAPI("/api/1.0/buildings/", {
            "last_updated_lt": last_updated_lt,
            "last_updated_gt": last_updated_gt,
            "first_added_lt": first_added_lt,
            "first_added_gt": first_added_gt,
            "custom_fields_and": custom_fields_and,
            "custom_fields_or": custom_fields_or,
        })

        names = []
        for device in response["buildings"]:
            names.append(device["name"])

        return names
