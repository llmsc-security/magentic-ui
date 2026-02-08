#!/usr/bin/env python3
"""
Tutorial PoC - HTTP API Test Client for Microsoft Magentic-UI FastAPI

This script demonstrates how to interact with the Magentic-UI API endpoints.
Run this after starting the Docker container to test the API functionality.

Usage:
    python tutorial_poc.py

API endpoints tested:
    - GET /api/health - Health check
    - GET /api/version - Get API version
    - GET /api/sessions - List sessions
    - POST /api/sessions - Create new session
    - GET /api/teams - List teams
    - GET /api/plans - List plans
    - GET /api/runs - List runs
"""

import asyncio
import json
import requests
from typing import Optional, Dict, Any


class MagenticUIAPIClient:
    """
    HTTP API client for Magentic-UI FastAPI server.
    Default port is 11240 when running in Docker.
    """

    def __init__(self, host: str = "localhost", port: int = 11240, base_url: str = None):
        """
        Initialize the API client.

        Args:
            host: The hostname of the Magentic-UI server
            port: The port of the Magentic-UI server
            base_url: Custom base URL if provided
        """
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = f"http://{host}:{port}"

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

        print(f"Magentic-UI API Client initialized")
        print(f"Base URL: {self.base_url}")

    def check_health(self) -> Dict[str, Any]:
        """
        Check the health status of the Magentic-UI server.

        Returns:
            Dictionary containing health status information
        """
        endpoint = f"{self.base_url}/api/health"
        print(f"\n--- Health Check ---")
        print(f"Endpoint: GET {endpoint}")

        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            if data.get("status"):
                print("Health check: PASSED")
            else:
                print("Health check: FAILED")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def get_version(self) -> Dict[str, Any]:
        """
        Get the API version information.

        Returns:
            Dictionary containing version information
        """
        endpoint = f"{self.base_url}/api/version"
        print(f"\n--- Get API Version ---")
        print(f"Endpoint: GET {endpoint}")

        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def list_sessions(self) -> Dict[str, Any]:
        """
        List all sessions.

        Returns:
            Dictionary containing session list
        """
        endpoint = f"{self.base_url}/api/sessions"
        print(f"\n--- List Sessions ---")
        print(f"Endpoint: GET {endpoint}")

        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def create_session(self, session_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a new session.

        Args:
            session_data: Optional session configuration data

        Returns:
            Dictionary containing created session information
        """
        endpoint = f"{self.base_url}/api/sessions"
        print(f"\n--- Create Session ---")
        print(f"Endpoint: POST {endpoint}")

        if session_data is None:
            session_data = {
                "name": "test-session",
                "description": "Test session created via API"
            }

        print(f"Request Data: {json.dumps(session_data, indent=2)}")

        try:
            response = self.session.post(endpoint, json=session_data)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def list_teams(self) -> Dict[str, Any]:
        """
        List all teams.

        Returns:
            Dictionary containing team list
        """
        endpoint = f"{self.base_url}/api/teams"
        print(f"\n--- List Teams ---")
        print(f"Endpoint: GET {endpoint}")

        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def list_plans(self) -> Dict[str, Any]:
        """
        List all plans.

        Returns:
            Dictionary containing plan list
        """
        endpoint = f"{self.base_url}/api/plans"
        print(f"\n--- List Plans ---")
        print(f"Endpoint: GET {endpoint}")

        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def list_runs(self) -> Dict[str, Any]:
        """
        List all runs.

        Returns:
            Dictionary containing run list
        """
        endpoint = f"{self.base_url}/api/runs"
        print(f"\n--- List Runs ---")
        print(f"Endpoint: GET {endpoint}")

        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            data = response.json()

            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"error": str(e)}

    def get_websocket_url(self) -> str:
        """
        Get the WebSocket URL for real-time communication.

        Returns:
            WebSocket URL string
        """
        # WebSocket URLs use ws:// or wss:// instead of http://
        if self.base_url.startswith("http://"):
            return self.base_url.replace("http://", "ws://") + "/ws"
        elif self.base_url.startswith("https://"):
            return self.base_url.replace("https://", "wss://") + "/ws"
        return self.base_url + "/ws"


async def test_websocket_connection(client: MagenticUIAPIClient):
    """
    Test WebSocket connection to the server.

    Args:
        client: MagenticUIAPIClient instance
    """
    import websockets

    ws_url = client.get_websocket_url()
    print(f"\n--- WebSocket Test ---")
    print(f"WebSocket URL: {ws_url}")

    try:
        async with websockets.connect(ws_url) as websocket:
            print("WebSocket connection established!")

            # Send a test message
            test_message = json.dumps({"type": "ping"})
            await websocket.send(test_message)
            print(f"Sent: {test_message}")

            # Receive response
            response = await websocket.recv()
            print(f"Received: {response}")

            return {"status": "success", "websocket": ws_url}
    except Exception as e:
        print(f"WebSocket error: {e}")
        return {"status": "error", "error": str(e)}


def main():
    """
    Main function to run API tests.
    """
    print("=" * 60)
    print("Microsoft Magentic-UI API Test Client")
    print("=" * 60)

    # Initialize client
    # Change host/port if running with different configuration
    client = MagenticUIAPIClient(host="localhost", port=11240)

    # Run API tests
    results = {}

    # 1. Health check
    results["health"] = client.check_health()

    # 2. Get version
    results["version"] = client.get_version()

    # 3. List sessions
    results["sessions"] = client.list_sessions()

    # 4. List teams
    results["teams"] = client.list_teams()

    # 5. List plans
    results["plans"] = client.list_plans()

    # 6. List runs
    results["runs"] = client.list_runs()

    # 7. Create session (optional - uncomment if needed)
    # results["create_session"] = client.create_session()

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    for test_name, result in results.items():
        status = "PASSED" if result.get("status") or "error" not in result else "FAILED"
        print(f"{test_name}: {status}")

    # Print connection info
    print("\n" + "=" * 60)
    print("Connection Information")
    print("=" * 60)
    print(f"API Base URL: {client.base_url}")
    print(f"WebSocket URL: {client.get_websocket_url()}")
    print(f"API Docs: {client.base_url}/api/docs")
    print(f"FastAPI Docs: {client.base_url}/docs")

    return results


if __name__ == "__main__":
    main()
