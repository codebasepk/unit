class Unit:
    def _construct_unit_section(self, description, after, before):
        section = f"""
[Unit]
Description={description}"""
        if after:
            section += f"""
After='{after}'"""
        if before:
            section += f"""
Before='{before}'"""

        section += """
        """
        return section

    def _construct_service_section(self, command, type, restart, user, stop, group, directory, bus_name, remain, notify):
        section = f"""
[Service]
Type={type}
ExecStart='{command}'"""

        if stop:
            section += f"""
ExecStop='{stop}'"""

        if restart:
            section += f"""
Restart={restart}"""

        if user:
            section += f"""
User={user}"""

        if group:
            section += f"""
Group={group}"""

        if directory:
            section += f"""
WorkingDirectory={directory}"""

        if bus_name:
            section += f"""
BusName={bus_name}"""

        if remain:
            section += f"""
RemainAfterExit={remain}"""

        if notify:
            section += f"""
NotifyAccess={notify}"""

        section += """
        """
        return section

    def _construct_install_section(self, wanted_by='multi-user.target'):
        section = f"""
[Install]
WantedBy={wanted_by}
        """

        return section

    def construct(self, description, command, type='simple', restart=None, user=None, stop=None, after=None,
                  before=None, group=None, directory=None, bus_name=None, remain_status=None, notify=None):
        unit_section = self._construct_unit_section(description, after, before)
        service_section = self._construct_service_section(command, type, restart, user, stop, group, directory,
                                                          bus_name, remain_status, notify)
        install_section = self._construct_install_section()

        result = unit_section + service_section + install_section

        return result
