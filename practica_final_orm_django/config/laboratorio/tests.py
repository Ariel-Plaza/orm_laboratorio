from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio prueba",
            ciudad="Santiago",
            pais="Chile"
        )
        print(f"Laboratorio de prueba creado: {cls.laboratorio}")

    def test_str_method(self):
        print(f"Probando el método __str__ de laboratorio: {LaboratorioModelTest.laboratorio}")
        self.assertEqual(str(LaboratorioModelTest.laboratorio), "Laboratorio prueba")
        print("Test __str__ pasó correctamente.")

    def test_datos_base_de_datos(self):
        laboratorio = Laboratorio.objects.get(id=LaboratorioModelTest.laboratorio.id)

        print(f"Verificando datos de laboratorio en base de datos: {laboratorio}")
        print(f"Nombre esperado: 'Laboratorio prueba', Ciudad: 'Santiago', País: 'Chile'")
        
        self.assertEqual(laboratorio.nombre, "Laboratorio prueba")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")
        self.assertEqual(laboratorio, LaboratorioModelTest.laboratorio)
        print("Test de datos base de datos pasó correctamente.")

class LaboratorioViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Clínico",
            ciudad="Santiago",
            pais="Chile"
        )
        print(f"Laboratorio de prueba creado para vistas: {cls.laboratorio}")

    def test_url_responde_http_200(self):
        url = reverse('laboratorio:laboratorio_index') 
        response = self.client.get(url)
        print(f"Probando URL: {url}, Respuesta HTTP: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        print("Test de URL con respuesta HTTP 200 pasó correctamente.")

    def test_url_responde_http_200_y_plantilla_correcta(self):
        url = reverse('laboratorio:laboratorio_index')
        response = self.client.get(url)
        
        print(f"Probando URL: {url}, Respuesta HTTP: {response.status_code}")
        print(f"Plantilla utilizada: 'laboratorio/ver_laboratorios.html'")
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/ver_laboratorios.html')
        
        self.assertContains(response, self.laboratorio.nombre)
        self.assertContains(response, self.laboratorio.ciudad)
        self.assertContains(response, self.laboratorio.pais)
        print("Test de URL, plantilla correcta y contenido esperado pasó correctamente.")
