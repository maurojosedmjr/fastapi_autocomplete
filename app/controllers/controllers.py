import json
import os
from typing import Any, Dict, List
from unicodedata import normalize

import cachebox

_current_path: str = os.path.abspath(os.getcwd())


def normalize_string(txt):
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII").lower()


@cachebox.cached(cachebox.TTLCache(0, ttl=8 * 3600))
def search_municipio(query: str) -> List[Dict[str, Any]]:
    with open(f"{_current_path}/app/data/municipios.json", "r") as fp:
        data: Dict[str, Any] = json.load(fp)
    ans: List[Dict[str, Any]] = list(
        filter(
            lambda item, prefix=normalize_string(query): prefix
            in item.get("slugs", []),
            data["data"],
        )
    )
    return ans
