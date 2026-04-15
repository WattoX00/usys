import os
import stat
from .functions import Functions

class PermissionFunctions():

    @staticmethod
    def viewPermissions():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        print(f"\nPermissions for: {path}\n")

        Functions.executeCmd(["ls", "-ld", path])

        print("\nACL Permissions:")
        Functions.executeCmd(["getfacl", path], check=False)


    @staticmethod
    def chmodPermissions():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        while True:
            perm = input("Enter chmod permission (example 755): ").strip()

            if perm.isdigit() and len(perm) in (3,4):
                break

            print("Invalid permission format.")

        Functions.executeCmd(["sudo", "chmod", perm, path])

        print("Permissions updated.")


    @staticmethod
    def changeOwner():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        username = Functions.userName()

        Functions.executeCmd(["sudo", "chown", username, path])

        print(f"Owner changed to '{username}'.")


    @staticmethod
    def changeGroup():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        groups = Functions.groupName()

        if not groups:
            return

        group = groups[0]

        Functions.executeCmd(["sudo", "chown", f":{group}", path])

        print(f"Group changed to '{group}'.")


    @staticmethod
    def addUserPermission():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        username = Functions.userName()

        while True:
            perms = input("Permissions (rwx combination, example rwx or rx): ").strip()

            valid = set("rwx")

            if set(perms).issubset(valid):
                break

            print("Invalid permission format.")

        Functions.executeCmd(
            ["sudo", "setfacl", "-m", f"u:{username}:{perms}", path]
        )

        print(f"ACL permission added for user '{username}'.")


    @staticmethod
    def addGroupPermission():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        groups = Functions.groupName()

        if not groups:
            return

        group = groups[0]

        while True:
            perms = input("Permissions (rwx combination, example rwx or rx): ").strip()

            valid = set("rwx")

            if set(perms).issubset(valid):
                break

            print("Invalid permission format.")

        Functions.executeCmd(
            ["sudo", "setfacl", "-m", f"g:{group}:{perms}", path]
        )

        print(f"ACL permission added for group '{group}'.")


    @staticmethod
    def removeUserPermission():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        username = Functions.userName()

        Functions.executeCmd(
            ["sudo", "setfacl", "-x", f"u:{username}", path]
        )

        print(f"ACL permission removed for user '{username}'.")


    @staticmethod
    def removeGroupPermission():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        groups = Functions.groupName()

        if not groups:
            return

        group = groups[0]

        Functions.executeCmd(
            ["sudo", "setfacl", "-x", f"g:{group}", path]
        )

        print(f"ACL permission removed for group '{group}'.")


    @staticmethod
    def recursivePermissions():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        while True:
            perm = input("Enter recursive chmod permission (example 755): ").strip()

            if perm.isdigit() and len(perm) in (3,4):
                break

            print("Invalid permission format.")

        Functions.executeCmd(
            ["sudo", "chmod", "-R", perm, path]
        )

        print("Recursive permissions updated.")


    @staticmethod
    def recursiveOwner():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        username = Functions.userName()

        Functions.executeCmd(
            ["sudo", "chown", "-R", username, path]
        )

        print(f"Recursive owner set to '{username}'.")


    @staticmethod
    def recursiveGroup():
        path = Functions.folder(must_exist=True)

        if not path:
            return

        groups = Functions.groupName()

        if not groups:
            return

        group = groups[0]

        Functions.executeCmd(
            ["sudo", "chown", "-R", f":{group}", path]
        )

        print(f"Recursive group set to '{group}'.")

    @staticmethod
    def createHardLink():
        print("\nCreate HARD link")

        source = Functions.folder(must_exist=True)
        if not source:
            return

        print("Select destination directory:")
        dest_dir = Functions.folder(must_exist=True)
        if not dest_dir:
            return

        link_name = input("Hard link name: ").strip()

        if not link_name:
            print("Link name cannot be empty.")
            return

        dest_path = os.path.join(dest_dir, link_name)

        Functions.executeCmd(
            ["sudo", "ln", source, dest_path]
        )

        print(f"Hard link created: {dest_path}")


    @staticmethod
    def createSoftLink():
        print("\nCreate SOFT (symbolic) link")

        source = Functions.folder(must_exist=True)
        if not source:
            return

        print("Select destination directory:")
        dest_dir = Functions.folder(must_exist=True)
        if not dest_dir:
            return

        link_name = input("Soft link name: ").strip()

        if not link_name:
            print("Link name cannot be empty.")
            return

        dest_path = os.path.join(dest_dir, link_name)

        Functions.executeCmd(
            ["sudo", "ln", "-s", source, dest_path]
        )

        print(f"Soft link created: {dest_path}")

    @staticmethod
    def helptext():
        print("""
                PERMISSION MANAGEMENT
        view            (v)     View file/folder permissions
        chmod           (c)     Change permissions (chmod)
        chown           (co)    Change owner
        chgrp           (cg)    Change group

                  ACL USER PERMISSIONS
        adduser         (au)    Add ACL permission for user
        rmuser          (ru)    Remove ACL permission for user

                 ACL GROUP PERMISSIONS
        addgroup        (ag)    Add ACL permission for group
        rmgroup         (rg)    Remove ACL permission for group

                 RECURSIVE PERMISSIONS
        rchmod          (rc)    Recursively change permissions
        rchown          (rco)   Recursively change owner
        rchgrp          (rcg)   Recursively change group

        LINK MANAGEMENT
        hardlink       (hl)    Create hard link
        softlink       (sl)    Create symbolic link
        
                    HELP & EXIT
        help            (h)     Show this help text
        quit            (q)     Quit the program
        """)
