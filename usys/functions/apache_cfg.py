from .Functions import Functions
import shutil

class ApacheFunctions:

    @staticmethod
    def detectPackageManager():
        managers = [
            ("apt", ["apt-get", "apt"]),
            ("dnf", ["dnf"]),
            ("yum", ["yum"]),
            ("pacman", ["pacman"]),
            ("zypper", ["zypper"]),
            ("apk", ["apk"]),
            ("xbps", ["xbps-install"]),
            ("eopkg", ["eopkg"]),
            ("emerge", ["emerge"]),
            ("nix", ["nix-env"])
        ]

        for manager, binaries in managers:
            for binary in binaries:
                if shutil.which(binary):
                    return manager

        return None


    @staticmethod
    def installApacheBasic():
        manager = ApacheFunctions.detectPackageManager()

        if not manager:
            print("No supported package manager detected.")
            return

        packages = {
            "apt": ["apache2"],
            "dnf": ["httpd"],
            "yum": ["httpd"],
            "pacman": ["apache"],
            "zypper": ["apache2"],
            "apk": ["apache2"],
            "xbps": ["apache"],
            "eopkg": ["apache"],
            "emerge": ["www-servers/apache"],
            "nix": ["nixpkgs.apacheHttpd"]
        }

        if manager == "apt":
            if not Functions.executeCmd(["sudo", "apt-get", "update"]):
                return
            cmd = ["sudo", "apt-get", "install", "-y"] + packages["apt"]

        elif manager == "pacman":
            cmd = ["sudo", "pacman", "-Sy", "--noconfirm"] + packages["pacman"]

        elif manager == "apk":
            cmd = ["sudo", "apk", "add"] + packages["apk"]

        elif manager == "xbps":
            cmd = ["sudo", "xbps-install", "-Sy"] + packages["xbps"]

        elif manager == "dnf":
            cmd = ["sudo", "dnf", "install", "-y"] + packages["dnf"]

        elif manager == "yum":
            cmd = ["sudo", "yum", "install", "-y"] + packages["yum"]

        elif manager == "zypper":
            cmd = ["sudo", "zypper", "install", "-y"] + packages["zypper"]

        elif manager == "eopkg":
            cmd = ["sudo", "eopkg", "install", "-y"] + packages["eopkg"]

        elif manager == "emerge":
            cmd = ["sudo", "emerge"] + packages["emerge"]

        elif manager == "nix":
            cmd = ["nix-env", "-iA"] + packages["nix"]

        else:
            print("Unsupported package manager.")
            return

        if Functions.executeCmd(cmd):
            print("Apache installed successfully.")


    @staticmethod
    def installApacheExtras():
        manager = ApacheFunctions.detectPackageManager()

        if not manager:
            print("No supported package manager detected.")
            return

        packages = {
            "apt": [
                "apache2-utils",
                "libapache2-mod-php",
                "certbot",
                "python3-certbot-apache",
                "libapache2-mod-security2"
            ],
            "dnf": [
                "httpd-tools",
                "mod_ssl",
                "php",
                "certbot",
                "python3-certbot-apache",
                "mod_security"
            ],
            "yum": [
                "httpd-tools",
                "mod_ssl",
                "php",
                "certbot",
                "python3-certbot-apache",
                "mod_security"
            ],
            "pacman": [
                "php-apache",
                "certbot"
            ],
            "zypper": [
                "apache2-utils",
                "apache2-mod_php",
                "certbot",
                "python3-certbot-apache",
                "apache2-mod_security2"
            ],
            "apk": [
                "apache2-utils",
                "php82-apache2",
                "certbot"
            ],
            "xbps": [
                "apache-utils",
                "php-apache",
                "certbot"
            ],
            "eopkg": [
                "apache-utils",
                "php",
                "certbot"
            ],
            "emerge": [
                "dev-lang/php",
                "app-crypt/certbot"
            ],
            "nix": [
                "nixpkgs.php",
                "nixpkgs.certbot"
            ]
        }

        if manager == "apt":
            if not Functions.executeCmd(["sudo", "apt-get", "update"]):
                return
            cmd = ["sudo", "apt-get", "install", "-y"] + packages["apt"]

        elif manager == "pacman":
            cmd = ["sudo", "pacman", "-Sy", "--noconfirm"] + packages["pacman"]

        elif manager == "apk":
            cmd = ["sudo", "apk", "add"] + packages["apk"]

        elif manager == "xbps":
            cmd = ["sudo", "xbps-install", "-Sy"] + packages["xbps"]

        elif manager == "dnf":
            cmd = ["sudo", "dnf", "install", "-y"] + packages["dnf"]

        elif manager == "yum":
            cmd = ["sudo", "yum", "install", "-y"] + packages["yum"]

        elif manager == "zypper":
            cmd = ["sudo", "zypper", "install", "-y"] + packages["zypper"]

        elif manager == "eopkg":
            cmd = ["sudo", "eopkg", "install", "-y"] + packages["eopkg"]

        elif manager == "emerge":
            cmd = ["sudo", "emerge"] + packages["emerge"]

        elif manager == "nix":
            cmd = ["nix-env", "-iA"] + packages["nix"]

        else:
            print("Unsupported package manager.")
            return

        if Functions.executeCmd(cmd):
            print("Apache additional packages installed successfully.")

    @staticmethod
    def apacheStart():
        cmd = ["sudo", "systemctl", "start", "apache2"]
        if Functions.executeCmd(cmd):
            print("Apache started.")

    @staticmethod
    def apacheStop():
        cmd = ["sudo", "systemctl", "stop", "apache2"]
        if Functions.executeCmd(cmd):
            print("Apache stopped.")

    @staticmethod
    def apacheRestart():
        cmd = ["sudo", "systemctl", "restart", "apache2"]
        if Functions.executeCmd(cmd):
            print("Apache restarted.")

    @staticmethod
    def apacheStatus():
        cmd = ["systemctl", "status", "apache2"]
        Functions.executeCmd(cmd, check=False)

    @staticmethod
    def apacheConfigTest():
        cmd = ["sudo", "apache2ctl", "configtest"]
        result = Functions.executeCmd(cmd, capture=True)

        if result:
            print(result.stdout)

    @staticmethod
    def apacheCreateTestSite():
        import os

        site_name = input("Site name: ").strip().lower()

        if not site_name:
            print("Invalid site name.")
            return

        site_path = f"/var/www/{site_name}"

        if os.path.exists(site_path):
            print("Site already exists.")
            return

        Functions.executeCmd(["sudo", "mkdir", "-p", site_path])

        html = f"<h1>{site_name} works!</h1>"

        Functions.executeCmd([
            "sudo", "bash", "-c",
            f"echo '{html}' > {site_path}/index.html"
        ])

        print(f"Test site created at {site_path}")

    @staticmethod
    def apacheCreateVHost():
        import os

        domain = input("Domain: ").strip().lower()

        if not domain:
            print("Invalid domain.")
            return

        docroot = f"/var/www/{domain}"

        config = f"""
    <VirtualHost *:80>
        ServerName {domain}

        DocumentRoot {docroot}

        <Directory {docroot}>
            AllowOverride All
            Require all granted
        </Directory>

        ErrorLog ${{APACHE_LOG_DIR}}/{domain}_error.log
        CustomLog ${{APACHE_LOG_DIR}}/{domain}_access.log combined
    </VirtualHost>
    """

        config_path = f"/etc/apache2/sites-available/{domain}.conf"

        Functions.executeCmd([
            "sudo", "bash", "-c",
            f"echo '{config}' > {config_path}"
        ])

        print(f"VirtualHost created: {config_path}")

    @staticmethod
    def apacheEnableSite():
        site = input("Site config name (example.conf): ").strip()

        cmd = ["sudo", "a2ensite", site]

        if Functions.executeCmd(cmd):
            print(f"Site '{site}' enabled.")

    @staticmethod
    def apacheDisableSite():
        site = input("Site config name: ").strip()

        cmd = ["sudo", "a2dissite", site]

        if Functions.executeCmd(cmd):
            print(f"Site '{site}' disabled.")

    @staticmethod
    def apacheAccessLog():
        cmd = ["sudo", "tail", "-n", "50", "/var/log/apache2/access.log"]
        Functions.executeCmd(cmd)

    @staticmethod
    def apacheErrorLog():
        cmd = ["sudo", "tail", "-n", "50", "/var/log/apache2/error.log"]
        Functions.executeCmd(cmd)

    @staticmethod
    def helptext():
        print("""
               APACHE COMMANDS
        install      (i)       Install Apache
        extras       (x)       Install Apache extras (PHP, Certbot, etc.)
        start        (st)      Start Apache
        stop         (sp)      Stop Apache
        restart      (r)       Restart Apache
        status       (ss)      Show Apache status

               SITE MANAGEMENT
        testsite     (ts)      Create simple test website
        vhost        (vh)      Create VirtualHost
        enable       (en)      Enable site
        disable      (di)      Disable site

                 HELP & EXIT
        helpf        (hf)      Full help menu
        quit         (q)       Quit the program
        """)

    @staticmethod
    def helptextfull():
        print("""
                APACHE MANAGEMENT
        install        (i)     Install Apache server
        extras         (x)     Install Apache extras (PHP, Certbot, Security)
        start          (st)    Start Apache
        stop           (sp)    Stop Apache
        restart        (r)     Restart Apache
        status         (ss)    Show Apache service status

                CONFIGURATION
        configtest     (ct)    Test Apache configuration
        vhost          (vh)    Create VirtualHost configuration

                SITE MANAGEMENT
        testsite       (ts)    Create simple test website
        enable         (en)    Enable site
        disable        (di)    Disable site

                    LOGS
        accesslog      (al)    Show last 50 access log lines
        errorlog       (el)    Show last 50 error log lines

                 HELP & EXIT
        help           (h)     Show help menu
        quit           (q)     Quit the program
        """)
