import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutonomousBrowserVisualDiffRegressionClient

def main():
    client = AutonomousBrowserVisualDiffRegressionClient(tolerance_px=4)
    res = client.compute_visual_regression_diff()
    print("=== Autonomous Browser Visual Diff Regression Output ===")
    print(f"Status: {res['visual_diff_status']} (Regressions: {res['regressions_detected_count']}/{res['elements_evaluated_count']})")
    print("\nElement Deltas:")
    for d in res['element_deltas']:
        print(f"  - [{d['selector']}] Shift: {d['max_displacement_px']}px (Within Tolerance: {d['within_tolerance']})")

if __name__ == '__main__':
    main()
