# Copyright 2024 Yunseong Hwang
#
# Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

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
