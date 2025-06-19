"""
Contact Book

Tavsif:
    Bu dastur kontaktlar bilan ishlaydi — qo‘shish, ko‘rish, qidirish va
    email bo‘yicha filtrlash. Har bir kontakt "Ism|Telefon|Email" formatida
    list ichida string sifatida saqlanadi.
"""

from typing import List


def show_menu() -> None:
    """Konsolda foydalanuvchi uchun menyuni chiqaradi."""
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. ➕ Yangi kontakt qo‘shish")
    print("2. 📄 Barcha kontaktlarni ko‘rish")
    print("3. 🔍 Kontaktni ism bo‘yicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni ko‘rish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact: str) -> bool:
    """
    Kontakt formati to‘g‘ri yoki noto‘g‘ri ekanligini aniqlaydi.

    Args:
        contact (str): Kontakt string (masalan, "Ali|99890...|ali@gmail.com").

    Returns:
        bool: To‘g‘ri format bo‘lsa True, aks holda False.
    """
    qism = contact.split("|")
    if contact and len(qism) == 3:
        name, phone, email = qism
        # Ism, telefon va email formatini tekshirish
        if name and phone.isdigit() and "@" in email and "." in email:
            return True
        return False
    return False
    


def add_contact(contact_list: List[str]) -> None:
    """
    Yangi kontakt qo‘shadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    new_contact = input("Yangi kontaktni kiriting (Ism|Telefon|Email): ").strip()
    if not is_valid_contact(new_contact):
        print(" Kontakt formati noto‘g‘ri. Iltimos, 'Ism|Telefon|Email' formatida kiriting.")
        return
    else:
        contact_list.append(new_contact)
        print(f" Kontakt qo‘shildi: {new_contact}")


def list_contacts(contact_list: List[str]) -> None:
    """
    Kontaktlar ro‘yxatini konsolga chiqaradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    if not contact_list:
        print(" Kontaktlar ro‘yxati bo‘sh.")
        return

    print("\n Barcha kontaktlar:")
    for contact in contact_list:
        print(f" - {contact}")


def search_contact(contact_list: List[str]) -> None:
    """
    Foydalanuvchi kiritgan ism bo‘yicha kontaktlarni qidiradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    name = input("Qidiranadigan ismni kiriting:").strip()
    if not name:
        print(" Iltimos, ism kiriting.")
        return
    found_contacts = [contact for contact in contact_list if contact.startswith(name + "|")]
    if found_contacts:
        print("\n Topilgan kontaktlar:")
        for contact in found_contacts:
            print(f" - {contact}")
    else:
        print(" Topilmadi.")

def filter_gmail_contacts(contact_list: List[str]) -> None:
    """
    Faqat @gmail.com domeniga ega kontaktlarni ko‘rsatadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    gmail_contacts = [contact for contact in contact_list if "@gmail.com" in contact]
    if gmail_contacts:
        print("\n Faqat @gmail.com kontaktlar:")
        for contact in gmail_contacts:
            print(f" - {contact}")
    else:
        print(" @gmail.com kontaktlar topilmadi.")


def main() -> None:
    """
    Dasturning asosiy ishga tushirish funksiyasi.
    Menyu orqali foydalanuvchi tanlovini boshqaradi.
    """
    contacts: List[str] = []

    while True:
        show_menu()
        choice = input("Tanlov (1–5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("❗️Noto‘g‘ri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")


main()
