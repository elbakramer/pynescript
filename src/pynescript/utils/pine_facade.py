import pathlib

import requests
import tqdm


def list_builtin_scripts():
    url = "https://pine-facade.tradingview.com"
    path = "/pine-facade/list/"
    params = {"filter": "template"}
    response = requests.get(url + path, params=params, timeout=60)
    response.raise_for_status()
    result = response.json()
    return result


def get_script(script_id_part, version):
    url = "https://pine-facade.tradingview.com"
    path = f"/pine-facade/get/{requests.utils.quote(script_id_part)}/{version}"
    params = {"no_4xx": "false"}
    response = requests.get(url + path, params=params, timeout=60)
    response.raise_for_status()
    result = response.json()
    return result


def download_builtin_scripts(script_dir, encodig=None):
    script_dir = pathlib.Path(script_dir)

    if encodig is None:
        encoding = "utf-8"

    if not script_dir.exists():
        script_dir.mkdir(parents=True, exist_ok=True)

    script_name_replace_mapping = {
        " ": "_",
        "-": "_",
        "/": "_",
    }

    script_list = list_builtin_scripts()
    script_list_tqdm = tqdm.tqdm(script_list)

    for script_meta in script_list_tqdm:
        script_name = script_meta["scriptName"]
        script_id_part = script_meta["scriptIdPart"]
        script_version = script_meta["version"]

        script_list_tqdm.set_description(f"Downloading script [{script_name}]")

        script = get_script(script_id_part, script_version)
        script_source = script["source"]

        script_name_prefix = script_name.lower()

        for from_pattern, replace_to in script_name_replace_mapping.items():
            script_name_prefix = script_name_prefix.replace(from_pattern, replace_to)

        script_filename = f"{script_name_prefix}.pine"

        with open(script_dir / script_filename, "w", encoding=encoding) as f:
            f.write(script_source)
