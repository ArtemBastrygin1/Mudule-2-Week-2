import unittest


class Document:
    def __init__(self, printer_page):
        self._printer_page = printer_page

    def print_document(self):
        return self._printer_page.print_page(self)


class InkjetPrinter:
    def print_page(self):
        return f"Печать сообщения на струйном принтере!"


class LaserPrinter:
    def print_page(self):
        return f"Печать сообщения на лазерном принтере!"


class TestDocument(unittest.TestCase):
    def test_inkjet(self):
        obj1 = Document(InkjetPrinter)
        self.assertEqual(
            obj1.print_document(), "Печать сообщения на струйном принтере!"
        )

    def test_laser(self):
        obj1 = Document(LaserPrinter)
        self.assertEqual(
            obj1.print_document(), "Печать сообщения на лазерном принтере!"
        )
