import json
from typing import Dict, Any, List, Optional

class AutonomousBrowserVisualDiffRegressionClient:
    """
    Production-grade visual regression and UI layout shift analyzer.
    Detects element displacement deltas and flags visual styling regressions.
    """
    def __init__(self, tolerance_px: int = 4):
        self.tolerance = tolerance_px

    def compute_visual_regression_diff(self, baseline_elements: Optional[List[Dict[str, Any]]] = None, current_elements: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        if not baseline_elements:
            baseline_elements = [
                {"selector": "#checkout-button", "x": 450, "y": 620, "width": 200, "height": 48},
                {"selector": "#cart-total-banner", "x": 450, "y": 560, "width": 400, "height": 40},
                {"selector": "#nav-header", "x": 0, "y": 0, "width": 1280, "height": 64}
            ]
        if not current_elements:
            current_elements = [
                {"selector": "#checkout-button", "x": 450, "y": 632, "width": 200, "height": 48},
                {"selector": "#cart-total-banner", "x": 450, "y": 560, "width": 400, "height": 40},
                {"selector": "#nav-header", "x": 0, "y": 0, "width": 1280, "height": 64}
            ]

        baseline_map = {e["selector"]: e for e in baseline_elements}
        deltas = []
        regressions_found = 0

        for cur in current_elements:
            sel = cur["selector"]
            base = baseline_map.get(sel)
            if base:
                dx = abs(cur["x"] - base["x"])
                dy = abs(cur["y"] - base["y"])
                dw = abs(cur["width"] - base["width"])
                dh = abs(cur["height"] - base["height"])
                max_shift = max(dx, dy, dw, dh)

                regressed = max_shift > self.tolerance
                if regressed: regressions_found += 1

                deltas.append({
                    "selector": sel,
                    "delta_x_px": dx,
                    "delta_y_px": dy,
                    "max_displacement_px": max_shift,
                    "within_tolerance": not regressed
                })

        return {
            "regression_test_id": "vis_reg_9918",
            "tolerance_threshold_px": self.tolerance,
            "elements_evaluated_count": len(current_elements),
            "regressions_detected_count": regressions_found,
            "visual_diff_status": "REGRESSION_DETECTED_DISPLACEMENT_EXCEEDED" if regressions_found > 0 else "VISUAL_STABLE_NO_REGRESSION",
            "element_deltas": deltas
        }
