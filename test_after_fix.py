from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_web_routes_after_fix():
    """Тестирование всех маршрутов веб-интерфейса после исправления"""
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
    
    print("Тестирование маршрутов веб-интерфейса после исправлений:")
    for route in routes_to_test:
        response = client.get(route)
        status = "+" if response.status_code == 200 else "-"
        print(f"{status} {route} - Status: {response.status_code}")
    
    print("\nТестирование завершено!")
    
    
    print("\nПроверка содержимого страницы поддержки:")
    response = client.get("/web/support")
    if response.status_code == 200:
        content = response.text
        if "faq-question" in content and "chev" in content:
            print("+ Страница поддержки содержит элементы FAQ")
        else:
            print("- Страница поддержки НЕ содержит ожидаемые элементы FAQ")
        
        if "expanded" in content and "rotated" in content:
            print("+ Страница поддержки содержит классы для анимации FAQ")
        else:
            print("- Страница поддержки НЕ содержит классы для анимации FAQ")
    else:
        print("- Не удалось получить страницу поддержки")

if __name__ == "__main__":
    test_web_routes_after_fix()