from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
    }

class Vendedor(AbstractUserRole):
    avaible_permissions = {
        'realizar_venda': True,
    }