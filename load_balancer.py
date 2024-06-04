import subprocess

def update_traefik_config(config):
    with open('/path/to/traefik/config.toml', 'w') as f:
        f.write(config)
    subprocess.run(['systemctl', 'restart', 'traefik'])
