"""base code"""
import os
import subprocess
import random

from pyngrok import ngrok

try:
    COLAB_ENV = True
    from google.colab import drive  # type:ignore
except ImportError:
    COLAB_ENV = False


EXTENSIONS = [
    "ms-python.python",
    "jithurjacob.nbpreviewer",
    "njpwerner.autodocstring",
    "ms-python.vscode-pylance",
    "ms-vscode-remote.remote-wsl",
    "ms-python.anaconda-extension-pack",
    "donjayamanne.githistory",
    "bee.git-temporal-vscode",
    "kiteco.kite",
    "vscode-icons-team.vscode-icons",
]
# "julialang.language-julia"


class ColabCode:
    """[sets up code server on an ngrok link]"""

    def __init__(
        self, port=10000, password=None, mount_drive=False, add_extensions=None
    ):
        self.port = port
        self.password = int(random.random() * 1e4) if password is None else password
        self._mount = mount_drive
        self._install_code()
        self.extensions = EXTENSIONS
        if add_extensions is not None and add_extensions != []:
            if isinstance(add_extensions, list) and isinstance(add_extensions[0], str):
                self.extensions += add_extensions
            else:
                raise TypeError(
                    "You need to pass a list of string(s) e.g. ['ms-python.python']"
                )
        self._install_extensions()
        self._start_server()
        self._run_code()

    def _install_code(self):
        subprocess.run(
            ["wget", "https://code-server.dev/install.sh"],
            stdout=subprocess.PIPE,
            check=True,
        )
        subprocess.run(["sh", "install.sh"], stdout=subprocess.PIPE, check=True)

    def _install_extensions(self):
        """set check as False - otherwise non existing extension will give error"""
        for ext in self.extensions:
            subprocess.run(
                ["code-server", "--install-extension", f"{ext}"], check=False
            )

    def _start_server(self):
        active_tunnels = ngrok.get_tunnels()
        for tunnel in active_tunnels:
            public_url = tunnel.public_url
            ngrok.disconnect(public_url)
        url = ngrok.connect(port=self.port, options={"bind_tls": True})
        print(f"Code Server can be accessed on: {url}")

    def _run_code(self):
        os.system(f"fuser -n tcp -k {self.port}")
        _tele = "--disable-telemetry"
        if self._mount and COLAB_ENV:
            drive.mount("/content/drive")
        if self.password:
            code_cmd = (
                f"PASSWORD={self.password} code-server --port {self.port} {_tele}"
            )
        else:
            code_cmd = f"code-server --port {self.port} --auth none {_tele}"
        with subprocess.Popen(
            [code_cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
        ) as proc:
            print(f"Use password {self.password} to login")
            for line in proc.stdout:
                print(line, end="")
