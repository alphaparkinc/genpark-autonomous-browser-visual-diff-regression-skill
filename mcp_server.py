import json, sys
from client import AutonomousBrowserVisualDiffRegressionClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "visual-diff-regression", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "compute_visual_regression_diff", "description": "Detects bounding box displacement deltas and flags visual styling regressions."}]}}
    elif method == "tools/call":
        client = AutonomousBrowserVisualDiffRegressionClient()
        res = client.compute_visual_regression_diff()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AutonomousBrowserVisualDiffRegressionClient()
        print(json.dumps(client.compute_visual_regression_diff(), indent=2))
