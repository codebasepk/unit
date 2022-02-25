

class Unit:
    def _construct_unit_section(self, description):
        section = f"""
[Unit]
Description={description}
        """

        return section

    def _construct_service_section(self, command, type):
        section = f"""
[Service]
Type={type}
ExecStart={command}
        """

        return section

    def _construct_install_section(self, wanted_by='multi-user.target'):
        section = f"""
[Install]
WantedBy={wanted_by}
        """

        return section

    def construct(self, description, command, type='simple'):
        unit_section = self._construct_unit_section(description)
        service_section = self._construct_service_section(command, type)
        install_section = self._construct_install_section()

        result = unit_section + service_section + install_section

        return result
