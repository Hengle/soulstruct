from __future__ import annotations

__all__ = ["DrawParam"]

from dataclasses import dataclass

from soulstruct.base.params.param import Param


@dataclass(slots=True)
class DrawParam(Param):
    """`Param` with some extra methods that are specific to DrawParam tables."""

    def get_nonzero_entries(self, ignore_polyg=True):
        """Filters table entries and returns only those with a non-empty name that does not start with '0' (or,
        by default, 'PolyG', which I assume is cutscene-specific lighting). """
        if ignore_polyg:
            return {
                index: row for index, row in self.rows.items() if row.Name and not row.Name.startswith("0")
            }
        return {
            index: row
            for index, row in self.rows.items()
            if row.Name and not row.Name.startswith("0") and not row.Name.lower().startswith("polyg")
        }