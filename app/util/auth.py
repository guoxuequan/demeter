#!/usr/bin/python
# -*- coding:utf-8 -*-

import ldap

class LDAPTool:

    def __init__(self):

        self.ldap_server = 'ldap://xx.xx.xx.xx:389'
        self.ldap_bind_user = 'gitlab'
        self.ldap_bind_passwd = 'xxxx'
        self.ldap_base = 'cn=xxxx,dc=xxxx,dc=com'

        try:
            self.conn = ldap.initialize(self.ldap_server)
            self.conn.simple_bind_s(self.ldap_bind_user, self.ldap_bind_passwd)
        except Exception as e:
            print(e)                   

    def get_dn(self, uid=None):
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = "sAMAccountName=" + uid
        retrieveAttributes = None

        try:
            obj = self.conn
            ldap_result_id = obj.search(self.ldap_base, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = obj.result(ldap_result_id, 0)

            if result_type == ldap.RES_SEARCH_ENTRY:
                user_dn = result_data[0][0]
                return user_dn
            else:
                return 'None'
        except Exception as e:
            print(e)

    def valid_user(self, uid=None, password=None):
        obj = self.conn
        target_dn = self.get_dn(uid)
        try:
            if obj.simple_bind_s(target_dn, password):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def user_info(self, uid=None):
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = "sAMAccountName=" + uid
        retrieveAttributes = None

        try:
            obj = self.conn
            ldap_result_id = obj.search(self.ldap_base, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = obj.result(ldap_result_id, 0)

            if result_type == ldap.RES_SEARCH_ENTRY:
                return result_data[0][1]
        except Exception as e:
            print(e)


if __name__ == '__main__':
    obj2 = LDAPTool()
    print(obj2.valid_user("ddd", "passwd"))
