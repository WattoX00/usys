from .functions import Functions, HelpFunctions
from datetime import datetime
import os
import pwd
import grp
import subprocess

class UserFunctions:

    @staticmethod
    def userAdd():
        try:
            newUserName = Functions.userName(must_exist=False)

            cmd = ["sudo", "useradd"]

            homeQ = input(f'Do you want to add home directory [/home/{newUserName}] (Y/n) ').strip().lower()
            if homeQ in ("y", "yes", ""):
                cmd.append("-m")

            groupQ = input(f'Do you want to add ({newUserName}) to a group (Y/n) ').strip().lower()
            if groupQ in ("y", "yes", ""):
                groups = Functions.groupName()
                if not groups:
                    print("No valid groups selected.")
                    return

                if len(groups) == 1:
                    cmd += ["-g", groups[0]]
                else:
                    cmd += ["-G", ",".join(groups)]

            cmd.append(newUserName)
            Functions.executeCmd(cmd)

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error adding user: {e}")

    @staticmethod
    def deleteUser():
        try:
            username = Functions.userName(must_exist=True)
            cmd = ["sudo", "userdel", "-r", username]
            Functions.executeCmd(cmd)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error deleting user: {e}")

    @staticmethod
    def userPassword():
        try:
            username = Functions.userName(must_exist=True)
            cmd = ["sudo", "passwd", username]
            Functions.executeCmd(cmd)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error changing password: {e}")

    @staticmethod
    def appendToGroup():
        try:
            username = Functions.userName(must_exist=True)
            groups = Functions.groupName()

            if not groups:
                print("No valid groups selected.")
                return

            cmd = ["sudo", "usermod", "-aG", ",".join(groups), username]
            Functions.executeCmd(cmd)

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error appending to group: {e}")

    @staticmethod
    def removeFromGroup():
        try:
            username = Functions.userName(must_exist=True)
            groups = Functions.groupName()

            if not groups:
                print("No valid groups selected.")
                return

            for group in groups:
                cmd = ["sudo", "gpasswd", "-d", username, group]
                Functions.executeCmd(cmd)

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error removing from group: {e}")

    @staticmethod
    def changeName():
        try:
            old = Functions.userName(must_exist=True)
            new = input('New name: ').strip().lower()

            if not new:
                print("New username cannot be empty.")
                return

            try:
                pwd.getpwnam(new)
                print("Username already exists.")
                return
            except KeyError:
                pass

            cmd = ["sudo", "usermod", "-l", new, old]
            Functions.executeCmd(cmd)

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error changing username: {e}")

    @staticmethod
    def changeShell():
        try:
            username = Functions.userName(must_exist=True)
            shellname = input('Change shell full path (/bin/bash): ').strip()

            if not os.path.isfile(shellname):
                print("Shell path does not exist.")
                return

            if not os.access(shellname, os.X_OK):
                print("Shell is not executable.")
                return

            cmd = ["sudo", "usermod", "-s", shellname, username]
            Functions.executeCmd(cmd)

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error changing shell: {e}")

    @staticmethod
    def lockUser():
        try:
            username = Functions.userName(must_exist=True)
            cmd = ["sudo", "usermod", "-L", username]
            Functions.executeCmd(cmd)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error locking user: {e}")

    @staticmethod
    def unlockUser():
        try:
            username = Functions.userName(must_exist=True)
            cmd = ["sudo", "usermod", "-U", username]
            Functions.executeCmd(cmd)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error unlocking user: {e}")

    @staticmethod
    def setExp():
        try:
            username = Functions.userName(must_exist=True)

            while True:
                date = input('Exp day (YYYY-MM-DD): ').strip()
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")

            cmd = ["sudo", "chage", "-E", date, username]
            Functions.executeCmd(cmd)

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error setting expiration: {e}")

    @staticmethod
    def removeExp():
        try:
            username = Functions.userName(must_exist=True)
            cmd = ["sudo", "chage", "-E", "-1", username]
            Functions.executeCmd(cmd)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error removing expiration: {e}")

    def changeUserId():
        username = Functions.userName()

        while True:
            try:
                newid = int(input('New UID: '))

                if HelpFunctions.uidExists(newid):
                    print("UID already exists.")
                    continue

                break

            except ValueError:
                print("UID must be a number.")

        cmd = ["sudo", "usermod", "-u", str(newid), username]
        Functions.executeCmd(cmd)

    # help text
    def helpText():
        print("""
    Command       Alias   Description

    adduser       (au)    Create a new user
    deluser       (du)    Delete an existing user
    passwd        (pw)    Change user password
    chname        (cn)    Change username
    chshell       (cs)    Change user shell

    listusers     (lu)    List all users
    homedir       (hd)    View home directory

    help          (h)     Show help menu
    helpf         (hf)    Show full help menu
    quit          (q)     Quit the program
    """)

    def fullHelp():
        print("""
                USER MANAGEMENT
    adduser         (au)    Create a new user
    deluser         (du)    Delete an existing user
    chname          (cn)    Change username
    chuid           (uid)   Change user ID
    chshell         (cs)    Change user shell
    passwd          (pw)    Change user password
    lockuser        (luu)   Lock user account
    unlockuser      (ulu)   Unlock user account
    setexp          (se)    Set account expiration date
    rmexp           (re)    Remove account expiration
    appendgroup     (ag)    Add user to an existing group
    rmfgroup        (ar)    Remove user from a group

              INFORMATION & LISTING
    listusers       (lu)    List all users
    listusergroups  (lug)   List groups of a user
    homedir         (hd)    View home directory
    passinfo        (pi)    Show password information
    userlocked      (ul)    Check if user is locked
    userexpday      (ued)   Show user expiration day
    iduser          (idu)   Show user ID information
    getentuser      (gu)    Get user entry information

                  HELP & EXIT
    help            (h)     Show help menu
    helpf           (hf)    Show full help menu
    quit            (q)     Quit the program
    """)
