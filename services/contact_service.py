from typing import List
from models.contact import Contact


class ContactService:
    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact(self, name: str, phone: str, email: str) -> str:
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        return f"Contact {name} ajouté."

    def get_contacts(self) -> List[Contact]:
        return self.contacts

    def del_contact(self, name: str) -> str:
        for contact in ContactService.self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"Contact {name} supprimé"
            else:
                return f"Le contact {name} n'existe pas"