from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_web_routes():
    """Тестирование всех маршрутов веб-интерфейса"""
    routes_to_test = [
        "/web/index",
        "/web/profile", 
        "/web/support",
        "/web/ticket1",
        "/web/ticket2", 
        "/web/ticket3",
        "/web/ticket4",
        "/web/ticket5",
        "/web/ticket6",
        "/web/ticket7",
        "/web/ticket8",
        "/web/ticket9"
    ]
    
    print("Тестирование маршрутов веб-интерфейса:")
    for route in routes_to_test:
        response = client.get(route)
        status = "+" if response.status_code == 200 else "-"
        print(f"{status} {route} - Status: {response.status_code}")
    
    print("\nТестирование завершено!")

if __name__ == "__main__":
    test_web_routes()