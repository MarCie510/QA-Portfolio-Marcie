import pytest
from playwright.sync_api import expect

# 🟢 Happy Path (Smoke Test)
@pytest.mark.smoke
def test_valid_login(login_page):
    login_page.navigate_to_login()
    
    # NOTA: Para que este test pase en verde, necesitas registrar un usuario en automationexercise.com
    # y actualizar estos datos. Por ahora, dejamos datos dummy para probar el script.
    login_page.login("tu_email_real@ejemplo.com", "tu_password_real")
    
    # Validación: Buscamos el texto que aparece al loguearse correctamente
    expect(login_page.page.locator("text=Logged in as")).to_be_visible()

# 🔴 Edge Case (Negative Test)
@pytest.mark.edge_case
def test_invalid_login(login_page):
    login_page.navigate_to_login()
    login_page.login("usuario_inexistente@test.com", "clave_falsa")
    
    # Validación: Verificamos que el mensaje de error contenga la palabra "incorrect"
    msg = login_page.get_error_message()
    assert "incorrect" in msg
